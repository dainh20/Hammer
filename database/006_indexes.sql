-- =========================
-- USERS
-- =========================
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);

-- =========================
-- ITEMS
-- =========================
CREATE INDEX idx_items_seller ON items(seller_id);
CREATE INDEX idx_items_category ON items(category_id);

-- =========================
-- AUCTIONS
-- =========================
CREATE INDEX idx_auctions_seller ON auctions(seller_id);
CREATE INDEX idx_auctions_status ON auctions(status);
CREATE INDEX idx_auctions_time ON auctions(start_time, end_time);

-- =========================
-- BIDS (PARTITIONED TABLE)
-- =========================
-- IMPORTANT: tạo trên parent → apply cho partition mới
CREATE INDEX idx_bid_auction_created 
ON bid (auction_id, created_at DESC);

CREATE INDEX idx_bid_user_created 
ON bid (user_id, created_at DESC);

-- =========================
-- WALLET TRANSACTIONS (PARTITIONED)
-- =========================
CREATE INDEX idx_wallet_tx_user_created 
ON wallet_transactions (user_id, created_at DESC);

CREATE INDEX idx_wallet_tx_type 
ON wallet_transactions (type);

-- =========================
-- PAYMENTS (PARTITIONED)
-- =========================
CREATE INDEX idx_payments_auction 
ON payments (auction_id);

CREATE INDEX idx_payments_payer 
ON payments (payer_id);

CREATE INDEX idx_payments_payee 
ON payments (payee_id);

CREATE INDEX idx_payments_status 
ON payments (status);

-- =========================
-- WALLETS
-- =========================
CREATE INDEX idx_wallets_user 
ON wallets(user_id);

-- =========================
-- WALLET REQUESTS
-- =========================
CREATE INDEX idx_wallet_req_user 
ON wallet_requests(user_id);

CREATE INDEX idx_wallet_req_status 
ON wallet_requests(status);

CREATE INDEX idx_wallet_req_created 
ON wallet_requests(created_at DESC);

-- =========================
-- AUCTION WINNERS
-- =========================
CREATE INDEX idx_winner_user 
ON auction_winners(winner_id);