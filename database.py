from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "'postgresql://neondb_owner:npg_iV4tazvO0RBq@ep-mute-band-af56ugn1-pooler.c-2.us-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
