from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from typing import List
from models import (
    ContactSubmissionCreate, ContactSubmission, SuccessResponse, ErrorResponse,
    ProfileData, PersonalInfo, Experience, ExperienceCreate,
    Testimonial, TestimonialCreate, TruffleExpertise, TruffleExpertiseCreate,
    SubmissionStatus
)
from database import db_manager
import logging
from datetime import datetime, timedelta
import asyncio
from collections import defaultdict

logger = logging.getLogger(__name__)

# Rate limiting storage (in production, use Redis)
rate_limit_storage = defaultdict(list)

def check_rate_limit(ip_address: str, max_requests: int = 3, time_window: int = 3600):
    """Check if IP address has exceeded rate limit"""
    now = datetime.utcnow()
    requests = rate_limit_storage[ip_address]
    
    # Remove old requests outside time window
    requests[:] = [req_time for req_time in requests if (now - req_time).seconds < time_window]
    
    if len(requests) >= max_requests:
        return False
    
    requests.append(now)
    return True

router = APIRouter(prefix="/api")

# Contact Form Routes
@router.post("/contact", response_model=SuccessResponse)
async def submit_contact_form(
    submission: ContactSubmissionCreate,
    request: Request
):
    try:
        # Get client IP and user agent
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent", "")
        
        # Rate limiting
        if not check_rate_limit(client_ip):
            raise HTTPException(
                status_code=429,
                detail="Too many requests. Please try again later."
            )
        
        # Create submission
        contact = await db_manager.create_contact_submission(
            submission, 
            ip_address=client_ip,
            user_agent=user_agent
        )
        
        logger.info(f"New contact submission from {submission.email}")
        
        return SuccessResponse(
            data={"id": contact.id},
            message="Thank you for your message! I'll get back to you within 24 hours."
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating contact submission: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/contact", response_model=List[ContactSubmission])
async def get_contact_submissions():
    """Get all contact submissions (admin only in production)"""
    try:
        submissions = await db_manager.get_contact_submissions()
        return submissions
    except Exception as e:
        logger.error(f"Error fetching contact submissions: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch("/contact/{submission_id}/status")
async def update_submission_status(
    submission_id: str,
    status: SubmissionStatus
):
    try:
        success = await db_manager.update_submission_status(submission_id, status.value)
        if not success:
            raise HTTPException(status_code=404, detail="Submission not found")
        
        return SuccessResponse(message="Status updated successfully")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating submission status: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Profile Data Routes
@router.get("/profile")
async def get_profile():
    try:
        profile = await db_manager.get_profile_data()
        if not profile:
            # Return default data if none exists
            default_profile = {
                "personal": {
                    "name": "Robert Chang",
                    "title": "Managing Director & Chief Truffle Officer",
                    "company": "American Truffle Company",
                    "location": "San Francisco, California, United States",
                    "summary": "Senior global business leader in technology, truffle cultivation and trade. Results-driven Stanford MBA with extensive general management experience and technical background. Fluent in English, German, Mandarin Chinese and Japanese.",
                    "languages": ["English", "German", "Mandarin Chinese", "Japanese"],
                    "specialties": [
                        "Market Strategies", "Channel Marketing", "Product Marketing", "Business Development",
                        "Advertising", "Pricing", "Sales Promotions", "Distribution", "Corporate Communications",
                        "Alliance/Partnerships", "Contract Negotiations", "Sales Development", "Cross-cultural Teams",
                        "Team Leadership", "Marketing Management", "Mobile and Wireless", "Branding", "Lead Generation"
                    ]
                }
            }
            return SuccessResponse(data=default_profile, message="Profile data retrieved successfully")
        
        return SuccessResponse(data=profile.dict(), message="Profile data retrieved successfully")
    except Exception as e:
        logger.error(f"Error fetching profile data: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Experience Routes
@router.get("/experience")
async def get_experiences():
    try:
        experiences = await db_manager.get_experiences()
        if not experiences:
            # Return default experience data if none exists
            default_experiences = [
                {
                    "id": "1",
                    "company": "American Truffle Company",
                    "position": "Managing Director & Chief Truffle Officer",
                    "duration": "December 2007 - Present (17 years)",
                    "location": "San Francisco, California",
                    "description": "Founded and led innovative truffle cultivation company, developing scientific methods to grow European truffles sustainably. Pioneered ultra-fresh truffle distribution globally.",
                    "achievements": [
                        "Established first commercial truffle cultivation operation in North America",
                        "Developed proprietary scientific methods for truffle cultivation",
                        "Built global distribution network for ultra-fresh truffles",
                        "Led company to profitability within 3 years"
                    ],
                    "order": 0,
                    "isActive": True
                },
                {
                    "id": "2",
                    "company": "ActionRun, Inc.",
                    "position": "VP of Marketing; CEO",
                    "duration": "2010 - 2013 (3 years)",
                    "location": "Silicon Valley, California",
                    "description": "Led marketing strategy and later served as CEO for mobile technology startup.",
                    "achievements": [
                        "Grew user base by 400% in first year as VP Marketing",
                        "Successfully transitioned to CEO role during critical growth phase",
                        "Secured Series A funding of $5M",
                        "Established partnerships with major mobile carriers"
                    ],
                    "order": 1,
                    "isActive": True
                },
                {
                    "id": "3",
                    "company": "Yahoo!",
                    "position": "Director of Product Marketing",
                    "duration": "October 2007 - February 2009 (1 year 5 months)",
                    "location": "Sunnyvale, California",
                    "description": "Led product marketing initiatives for Yahoo's core products during critical transformation period.",
                    "achievements": [
                        "Managed product marketing for products serving 500M+ users",
                        "Led cross-functional teams across multiple time zones",
                        "Developed go-to-market strategies for mobile products",
                        "Improved user engagement metrics by 35%"
                    ],
                    "order": 2,
                    "isActive": True
                }
            ]
            return SuccessResponse(data=default_experiences, message="Experience data retrieved successfully")
        
        return SuccessResponse(data=[exp.dict() for exp in experiences], message="Experience data retrieved successfully")
    except Exception as e:
        logger.error(f"Error fetching experiences: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Testimonial Routes
@router.get("/testimonials")
async def get_testimonials():
    try:
        testimonials = await db_manager.get_testimonials()
        if not testimonials:
            # Return default testimonials if none exist
            default_testimonials = [
                {
                    "id": "1",
                    "name": "Sarah Williams",
                    "title": "Former CEO, TechVentures",
                    "content": "Robert's unique combination of technical expertise and business acumen is extraordinary. His ability to bridge cultures and markets made him invaluable to our global expansion.",
                    "avatar": "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=400&h=400&fit=crop&crop=face",
                    "order": 0,
                    "isActive": True
                },
                {
                    "id": "2",
                    "name": "Dr. Marcus Chen",
                    "title": "Research Director, Agricultural Sciences",
                    "content": "Robert's innovative approach to truffle cultivation has revolutionized the industry. His scientific rigor combined with business vision is truly remarkable.",
                    "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face",
                    "order": 1,
                    "isActive": True
                },
                {
                    "id": "3",
                    "name": "Lisa Park",
                    "title": "VP Marketing, Global Corp",
                    "content": "Working with Robert at Yahoo was transformative. His cross-cultural leadership and strategic thinking helped us navigate complex international markets successfully.",
                    "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=face",
                    "order": 2,
                    "isActive": True
                }
            ]
            return SuccessResponse(data=default_testimonials, message="Testimonials retrieved successfully")
        
        return SuccessResponse(data=[test.dict() for test in testimonials], message="Testimonials retrieved successfully")
    except Exception as e:
        logger.error(f"Error fetching testimonials: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Truffle Expertise Routes
@router.get("/expertise")
async def get_truffle_expertise():
    try:
        expertise = await db_manager.get_truffle_expertise()
        if not expertise:
            # Return default expertise data if none exists
            default_expertise = {
                "title": "Truffle Cultivation Innovation",
                "subtitle": "Pioneering Scientific Approach to European Truffle Cultivation",
                "description": "Combining advanced agricultural science with sustainable practices to revolutionize truffle cultivation in North America.",
                "achievements": [
                    "First commercial truffle cultivation in North America",
                    "Proprietary soil microbiome optimization techniques",
                    "Sustainable harvesting methods preserving ecosystem",
                    "Global distribution of ultra-fresh truffles within 48 hours",
                    "Partnership with Michelin-starred restaurants worldwide",
                    "Scientific publications on truffle mycorrhizal relationships"
                ],
                "metrics": [
                    {"label": "Years of Research", "value": "17+"},
                    {"label": "Truffle Varieties", "value": "8"},
                    {"label": "Global Partners", "value": "50+"},
                    {"label": "Harvest Success Rate", "value": "95%"}
                ]
            }
            return SuccessResponse(data=default_expertise)
        
        return SuccessResponse(data=expertise.dict())
    except Exception as e:
        logger.error(f"Error fetching truffle expertise: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")