from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker

Base = declarative_base()
engine = create_async_engine(
    "sqlite+aiosqlite:///database.db",
    connect_args={
        "check_same_thread": False,
    },
)

Session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
)
