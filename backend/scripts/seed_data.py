import sqlalchemy
from sqlalchemy.orm import Session

from app.config.db import engine, SessionLocal
from app import models
from app.models import User

models.Model.metadata.create_all(bind=engine)

print("# --- Create Users", end="")

users = [
    User(username="Alice"),
    User(username="Bob"),
    User(username="Robot"),
]
created_users = []
with SessionLocal() as session:
    for user in users:
        session.add(user)
        try:
            session.commit()
            created_users.append(user)
        except sqlalchemy.exc.IntegrityError:
            # Create if not exists
            session.rollback()

if created_users:
    print()
    print(f"\n# --- Created Users:", ",".join(user.username for user in created_users))
else:
    print(" (skipped)")
