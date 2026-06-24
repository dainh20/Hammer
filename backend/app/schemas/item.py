from pydantic import BaseModel


class ItemCreate(BaseModel):
    title: str
    description: str
    category_id: int | None = None
    condition: int


class ItemOut(BaseModel):
    id: int
    seller_id: int
    title: str
    description: str | None
    category_id: int | None
    condition: int

    class Config:
        from_attributes = True