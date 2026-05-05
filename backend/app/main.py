from fastapi import FastAPI
from app.api.routes import auth, users, auctions, bids, wallets, payments

app = FastAPI(title="Online Auction API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auctions.router, prefix="/auctions", tags=["auctions"])
app.include_router(bids.router, prefix="/bids", tags=["bids"])
app.include_router(wallets.router, prefix="/wallets", tags=["wallets"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])