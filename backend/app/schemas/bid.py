from pydantic import BaseModel


class BidCreate(BaseModel):
    auction_id: int
    bid_amount: int


class BidOut(BaseModel):
    id: int
    auction_id: int
    user_id: int
    bid_amount: int

    class Config:
        from_attributes = True