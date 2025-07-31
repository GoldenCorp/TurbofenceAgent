from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql+psycopg://postgres.ogntiglacqlqmtnaqgup:eMHk1x6wDb81PiHw@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres",
    echo=True,
    max_overflow=10,
    pool_size=50,
    pool_recycle=3600,
    pool_timeout=30,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
Base = declarative_base()

