from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    role: str


class UserCreate(UserBase):
    pass


class Login_User(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True