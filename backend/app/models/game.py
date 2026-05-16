from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base
import uuid

class Game(Base):
    """
    Cached game data from RAWG so we don't hammer their API on every page load.
    """
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)  # Using RAWG's integer ID
    title = Column(String, nullable=False)
    cover_image_url = Column(String)
    release_date = Column(String)

class UserGame(Base):
    """
    Handles our user backlogs, reviews, and ratings.
    """
    __tablename__ = "user_games"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False)
    game_id = Column(Integer, ForeignKey("games.id", ondelete="CASCADE"), nullable=False)
    
    # Backlog status
    status = Column(String, default="Want to Play") # "Want to Play", "Playing", "Completed"
    
    # Review components
    rating = Column(Integer, nullable=True) # 1-5
    review_text = Column(Text, nullable=True)
