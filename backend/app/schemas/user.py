from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    name: str
    email: EmailStr
    password: str
    phone: str
    address: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: int
    username: str
    name: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str