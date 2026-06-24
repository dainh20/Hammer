from pydantic import BaseModel
from datetime import datetime


class AuctionCreate(BaseModel):
    item_id: int
    starting_price: int
    reserve_price: int | None = None
    start_time: datetime
    end_time: datetime


class AuctionOut(BaseModel):
    auction_id: int
    item_id: int
    current_price: int | None
    status: str

    class Config:
        from_attributes = True