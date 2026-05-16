from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# asyncpg requires the scheme to be postgresql+asyncpg://
engine_url = settings.DATABASE_URL
if engine_url.startswith("postgres://"):
    engine_url = engine_url.replace("postgres://", "postgresql+asyncpg://", 1)
elif engine_url.startswith("postgresql://"):
    engine_url = engine_url.replace("postgresql://", "postgresql+asyncpg://", 1)

# Connect to database using async engine. NullPool bypasses connection cache issues with Supabase Pooler.
from sqlalchemy.pool import NullPool
engine = create_async_engine(engine_url, echo=False, poolclass=NullPool)

# Session factory
async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with async_session() as session:
        yield session
