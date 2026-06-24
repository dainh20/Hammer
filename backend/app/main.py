from fastapi import FastAPI

from app.api.routes import (
    auth,
    auctions,
    bids,
    wallets,
    items
)

app = FastAPI(
    title="Online Auction API"
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    auctions.router,
    prefix="/auctions",
    tags=["auctions"]
)

app.include_router(
    bids.router,
    prefix="/bids",
    tags=["bids"]
)

app.include_router(
    wallets.router,
    prefix="/wallets",
    tags=["wallets"]
)

app.include_router(
    items.router,
    prefix="/items",
    tags=["items"]
)