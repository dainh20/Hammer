from app.repositories import user_repo
from app.core.security import hash_password

def register_user(db, data):
    hashed = hash_password(data.password)
    return user_repo.create_user(db, data.username, data.email, hashed)