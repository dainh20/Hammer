from sqlalchemy.orm import Session
from sqlalchemy import text

def place_bid(db: Session, user_id: int, auction_id: int, amount: int):
    # IMPORTANT: dùng transaction
    db.execute(text("BEGIN"))

    # lock auction
    auction = db.execute(text("""
        SELECT * FROM auctions
        WHERE auction_id = :id
        FOR UPDATE
    """), {"id": auction_id}).fetchone()

    if not auction:
        raise Exception("Auction not found")

    if amount <= auction.current_price:
        raise Exception("Bid too low")

    # insert bid
    db.execute(text("""
        INSERT INTO bid (auction_id, user_id, bid_amount)
        VALUES (:a, :u, :amt)
    """), {"a": auction_id, "u": user_id, "amt": amount})

    # update price
    db.execute(text("""
        UPDATE auctions
        SET current_price = :amt
        WHERE auction_id = :id
    """), {"amt": amount, "id": auction_id})

    db.commit()