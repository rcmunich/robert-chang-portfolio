from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid

class InquiryType(str, Enum):
    BUSINESS_PARTNERSHIP = "Business Partnership"
    EXECUTIVE_OPPORTUNITY = "Executive Opportunity"
    TRUFFLE_COLLABORATION = "Truffle Collaboration"
    CONSULTING_SERVICES = "Consulting Services"
    OTHER = "Other"

class SubmissionStatus(str, Enum):
    NEW = "new"
    READ = "read"
    RESPONDED = "responded"

# Contact Form Models
class ContactSubmissionCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    subject: str = Field(..., min_length=5, max_length=200)
    message: str = Field(..., min_length=10, max_length=2000)
    inquiryType: InquiryType

class ContactSubmission(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    subject: str
    message: str
    inquiryType: InquiryType
    submittedAt: datetime = Field(default_factory=datetime.utcnow)
    status: SubmissionStatus = SubmissionStatus.NEW
    ipAddress: Optional[str] = None
    userAgent: Optional[str] = None

# Profile Models
class PersonalInfo(BaseModel):
    name: str
    title: str
    company: str
    location: str
    summary: str
    languages: List[str]
    specialties: List[str]

class ProfileData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    personal: PersonalInfo
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

# Experience Models
class ExperienceCreate(BaseModel):
    company: str = Field(..., min_length=1, max_length=200)
    position: str = Field(..., min_length=1, max_length=200)
    duration: str = Field(..., min_length=1, max_length=100)
    location: Optional[str] = Field(None, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    achievements: List[str] = []
    order: int = Field(default=0)
    isActive: bool = Field(default=True)

class Experience(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    company: str
    position: str
    duration: str
    location: Optional[str]
    description: str
    achievements: List[str]
    order: int
    isActive: bool

# Testimonial Models
class TestimonialCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=10, max_length=1000)
    avatar: Optional[str] = Field(None, max_length=500)
    order: int = Field(default=0)
    isActive: bool = Field(default=True)

class Testimonial(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    title: str
    content: str
    avatar: Optional[str]
    order: int
    isActive: bool

# Truffle Expertise Models
class ExpertiseMetric(BaseModel):
    label: str
    value: str

class TruffleExpertise(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    subtitle: str
    description: str
    achievements: List[str]
    metrics: List[ExpertiseMetric]
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class TruffleExpertiseCreate(BaseModel):
    title: str
    subtitle: str
    description: str
    achievements: List[str]
    metrics: List[ExpertiseMetric]

# Response Models
class SuccessResponse(BaseModel):
    success: bool = True
    data: Optional[dict] = None
    message: str

class ErrorResponse(BaseModel):
    success: bool = False
    error: dict