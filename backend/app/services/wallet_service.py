def approve_request(db, request_id):
    result = db.execute("""
        UPDATE wallet_requests
        SET status = 'approved'
        WHERE request_id = :id AND status = 'pending'
        RETURNING *
    """, {"id": request_id}).fetchone()

    if not result:
        raise Exception("Already processed")

    # update wallet
    db.execute("""
        UPDATE wallets
        SET balance = balance + :amt
        WHERE user_id = :uid
    """, {"amt": result.amount, "uid": result.user_id})

    db.commit()