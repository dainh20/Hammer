from pydantic import BaseModel


class WalletRequestCreate(BaseModel):
    amount: int
    type: str


class WalletOut(BaseModel):
    balance: int
    locked_balance: int

    class Config:
        from_attributes = True