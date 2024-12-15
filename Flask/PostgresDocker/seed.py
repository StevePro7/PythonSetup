from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Create database tables if they don't exist
    db.create_all()

    # Add some sample users
    if User.query.count() == 0:
        user1 = User(username="Alice")
        user2 = User(username="Bob")
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    print("Database seeded!")
