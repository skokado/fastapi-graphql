from pathlib import Path

import sqlalchemy


def main():
    from app.config.db import engine, sessionmaker
    from app.models import User, Model

    Model.metadata.create_all(bind=engine)

    print("# --- Create Users", end="")

    users = [
        User(username="Alice"),
        User(username="Bob"),
        User(username="Robot"),
    ]
    created_users = []
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    with Session() as session:
        for user in users:
            session.add(user)
            try:
                session.commit()
                session.refresh(user)
                created_users.append(user)
            except sqlalchemy.exc.IntegrityError:
                # Create if not exists
                session.rollback()

    if created_users:
        print()
        print(f"# --- Created Users:", ",".join(user.username for user in created_users))
    else:
        print(" (skipped)")


if __name__ == "__main__":
    import sys

    file_path = Path(__file__).parent
    root_dir = file_path.parent
    sys.path.insert(0, root_dir.as_posix())

    main()
