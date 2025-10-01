import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
from models import User, Ritual  # PostgreSQL models

# Load environment variables
load_dotenv()

# Connect to SQLite (source)
sqlite_engine = create_engine("sqlite:///instance/drt_data.db")
sqlite_session = Session(sqlite_engine)

# Connect to PostgreSQL (destination)
postgres_engine = create_engine(os.getenv("POSTGRES_URL"))
postgres_session = Session(postgres_engine)

# Read from SQLite
sqlite_users = sqlite_session.query(User).all()
sqlite_rituals = sqlite_session.query(Ritual).all()

# Migrate users
migrated_users = 0
for u in sqlite_users:
    try:
        postgres_session.add(User(email=u.email, password=u.password, name=u.name))
        migrated_users += 1
    except IntegrityError:
        postgres_session.rollback()  # skip duplicates
postgres_session.commit()

# Migrate rituals
migrated_rituals = 0
for r in sqlite_rituals:
    try:
        postgres_session.add(Ritual(
            user_id=r.user_id,
            date=r.date,
            begin_time=r.begin_time,
            finish_time=r.finish_time,
            comment=r.comment
        ))
        migrated_rituals += 1
    except IntegrityError:
        postgres_session.rollback()
postgres_session.commit()

print(f"Migrated {migrated_users} users and {migrated_rituals} rituals.")
