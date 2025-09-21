from motor.motor_asyncio import AsyncIOMotorClient
from typing import List, Optional
import os
from models import (
    ContactSubmission, ContactSubmissionCreate, ProfileData, PersonalInfo,
    Experience, ExperienceCreate, Testimonial, TestimonialCreate,
    TruffleExpertise, TruffleExpertiseCreate
)
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self):
        mongo_url = os.environ['MONGO_URL']
        self.client = AsyncIOMotorClient(mongo_url)
        self.db = self.client[os.environ['DB_NAME']]
        
    async def close(self):
        self.client.close()

    # Contact Submissions
    async def create_contact_submission(self, submission: ContactSubmissionCreate, ip_address: str = None, user_agent: str = None) -> ContactSubmission:
        contact_data = ContactSubmission(
            **submission.dict(),
            ipAddress=ip_address,
            userAgent=user_agent
        )
        
        result = await self.db.contact_submissions.insert_one(contact_data.dict())
        contact_data.id = str(result.inserted_id)
        return contact_data
    
    async def get_contact_submissions(self) -> List[ContactSubmission]:
        cursor = self.db.contact_submissions.find().sort("submittedAt", -1)
        submissions = []
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            submissions.append(ContactSubmission(**doc))
        return submissions
    
    async def update_submission_status(self, submission_id: str, status: str) -> bool:
        result = await self.db.contact_submissions.update_one(
            {"_id": submission_id},
            {"$set": {"status": status}}
        )
        return result.modified_count > 0

    # Profile Data
    async def get_profile_data(self) -> Optional[ProfileData]:
        doc = await self.db.profile_data.find_one()
        if doc:
            doc["id"] = str(doc["_id"])
            return ProfileData(**doc)
        return None
    
    async def update_profile_data(self, profile_data: ProfileData) -> ProfileData:
        profile_dict = profile_data.dict()
        profile_dict["updatedAt"] = datetime.utcnow()
        
        await self.db.profile_data.replace_one(
            {},
            profile_dict,
            upsert=True
        )
        return profile_data
    
    # Experience
    async def get_experiences(self) -> List[Experience]:
        cursor = self.db.experiences.find({"isActive": True}).sort("order", 1)
        experiences = []
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            experiences.append(Experience(**doc))
        return experiences
    
    async def create_experience(self, experience: ExperienceCreate) -> Experience:
        experience_data = Experience(**experience.dict())
        result = await self.db.experiences.insert_one(experience_data.dict())
        experience_data.id = str(result.inserted_id)
        return experience_data
    
    async def update_experience(self, experience_id: str, experience: ExperienceCreate) -> Optional[Experience]:
        result = await self.db.experiences.update_one(
            {"_id": experience_id},
            {"$set": experience.dict()}
        )
        if result.modified_count > 0:
            doc = await self.db.experiences.find_one({"_id": experience_id})
            if doc:
                doc["id"] = str(doc["_id"])
                return Experience(**doc)
        return None
    
    async def delete_experience(self, experience_id: str) -> bool:
        result = await self.db.experiences.update_one(
            {"_id": experience_id},
            {"$set": {"isActive": False}}
        )
        return result.modified_count > 0

    # Testimonials
    async def get_testimonials(self) -> List[Testimonial]:
        cursor = self.db.testimonials.find({"isActive": True}).sort("order", 1)
        testimonials = []
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            testimonials.append(Testimonial(**doc))
        return testimonials
    
    async def create_testimonial(self, testimonial: TestimonialCreate) -> Testimonial:
        testimonial_data = Testimonial(**testimonial.dict())
        result = await self.db.testimonials.insert_one(testimonial_data.dict())
        testimonial_data.id = str(result.inserted_id)
        return testimonial_data
    
    async def update_testimonial(self, testimonial_id: str, testimonial: TestimonialCreate) -> Optional[Testimonial]:
        result = await self.db.testimonials.update_one(
            {"_id": testimonial_id},
            {"$set": testimonial.dict()}
        )
        if result.modified_count > 0:
            doc = await self.db.testimonials.find_one({"_id": testimonial_id})
            if doc:
                doc["id"] = str(doc["_id"])
                return Testimonial(**doc)
        return None
    
    async def delete_testimonial(self, testimonial_id: str) -> bool:
        result = await self.db.testimonials.update_one(
            {"_id": testimonial_id},
            {"$set": {"isActive": False}}
        )
        return result.modified_count > 0

    # Truffle Expertise
    async def get_truffle_expertise(self) -> Optional[TruffleExpertise]:
        doc = await self.db.truffle_expertise.find_one()
        if doc:
            doc["id"] = str(doc["_id"])
            return TruffleExpertise(**doc)
        return None
    
    async def update_truffle_expertise(self, expertise: TruffleExpertiseCreate) -> TruffleExpertise:
        expertise_data = TruffleExpertise(**expertise.dict())
        expertise_dict = expertise_data.dict()
        
        await self.db.truffle_expertise.replace_one(
            {},
            expertise_dict,
            upsert=True
        )
        return expertise_data

# Global database instance
db_manager = DatabaseManager()