from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone
import uuid
from app.models.base import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    # We use UUID because Supabase Auth issues UUIDs for their users!
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    display_name = Column(String)
    bio = Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
