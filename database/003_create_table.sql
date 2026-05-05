-- =========================
-- USERS
-- =========================
CREATE TABLE users (
    user_id        BIGSERIAL PRIMARY KEY,
    username       VARCHAR(100) NOT NULL UNIQUE,
    name           VARCHAR(255),
    email          VARCHAR(255) NOT NULL UNIQUE,
    password_hash  TEXT NOT NULL,
    phone          VARCHAR(20),
    address        TEXT,
    status         VARCHAR(20) DEFAULT 'active'
        CHECK (status IN ('active', 'inactive', 'banned')),
    created_at     TIMESTAMPTZ DEFAULT NOW(),
    updated_at     TIMESTAMPTZ DEFAULT NOW()
);

-- =========================
-- CATEGORIES
-- =========================
CREATE TABLE categories (
    category_id BIGSERIAL PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    parent_id   BIGINT REFERENCES categories(category_id)
);

-- =========================
-- ITEMS
-- =========================
CREATE TABLE items (
    id           BIGSERIAL PRIMARY KEY,
    seller_id    BIGINT NOT NULL REFERENCES users(user_id),
    title        VARCHAR(255) NOT NULL,
    description  TEXT,
    category_id  BIGINT REFERENCES categories(category_id),
    condition    INT,
    created_at   TIMESTAMPTZ DEFAULT NOW(),
    updated_at   TIMESTAMPTZ DEFAULT NOW()
);

-- =========================
-- AUCTIONS
-- =========================
CREATE TABLE auctions (
    auction_id     BIGSERIAL PRIMARY KEY,
    item_id        BIGINT UNIQUE REFERENCES items(id),
    seller_id      BIGINT REFERENCES users(user_id),

    starting_price BIGINT NOT NULL CHECK (starting_price >= 0),
    reserve_price  BIGINT,
    current_price  BIGINT,

    start_time     TIMESTAMPTZ NOT NULL,
    end_time       TIMESTAMPTZ NOT NULL,

    status         VARCHAR(20) DEFAULT 'draft'
        CHECK (status IN ('draft', 'active', 'ended', 'cancelled')),

    created_at     TIMESTAMPTZ DEFAULT NOW(),

    CHECK (end_time > start_time),
    CHECK (current_price IS NULL OR current_price >= starting_price)
);

-- =========================
-- BIDS (PARTITIONED)
-- =========================
CREATE TABLE bid (
    id          BIGSERIAL,
    auction_id  BIGINT NOT NULL,
    user_id     BIGINT NOT NULL,
    bid_amount  BIGINT NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    PRIMARY KEY (id, created_at)
) PARTITION BY RANGE (created_at);

-- =========================
-- WALLET TRANSACTIONS (PARTITIONED)
-- =========================
CREATE TABLE wallet_transactions (
    transaction_id BIGSERIAL,
    user_id        BIGINT NOT NULL,
    amount         BIGINT NOT NULL,
    type           VARCHAR(50) NOT NULL,
    status         VARCHAR(20) NOT NULL DEFAULT 'pending' 
        CHECK (status IN ('pending', 'success', 'failed')),
    reference_id   BIGINT,
    created_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    PRIMARY KEY (transaction_id, created_at)
) PARTITION BY RANGE (created_at);

-- =========================
-- PAYMENTS (PARTITIONED)
-- =========================
CREATE TABLE payments (
    payment_id   BIGSERIAL,
    auction_id   BIGINT,
    payer_id     BIGINT,
    payee_id     BIGINT,
    amount       BIGINT NOT NULL,
    method       VARCHAR(20),
    status       VARCHAR(20) NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'success', 'failed')),
    paid_at      TIMESTAMPTZ,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    PRIMARY KEY (payment_id, created_at)
) PARTITION BY RANGE (created_at);

-- =========================
-- WALLETS
-- =========================
CREATE TABLE wallets (
    user_id        BIGINT PRIMARY KEY REFERENCES users(user_id),
    balance        BIGINT NOT NULL DEFAULT 0,
    locked_balance BIGINT NOT NULL DEFAULT 0,
    updated_at     TIMESTAMPTZ DEFAULT NOW()
);

-- =========================
-- WALLET REQUESTS
-- =========================
CREATE TABLE wallet_requests (
    request_id    BIGSERIAL PRIMARY KEY,
    user_id       BIGINT REFERENCES users(user_id),
    amount        BIGINT NOT NULL,
    type          VARCHAR(20) NOT NULL,
    status        VARCHAR(20) NOT NULL DEFAULT 'pending',
    note          TEXT,
    admin_id      BIGINT,
    processed_at  TIMESTAMPTZ,
    created_at    TIMESTAMPTZ DEFAULT NOW(),

    CHECK (type IN ('deposit', 'withdraw')),
    CHECK (status IN ('pending', 'approved', 'rejected'))
);

-- =========================
-- AUCTION WINNERS
-- =========================
CREATE TABLE auction_winners (
    auction_id      BIGINT PRIMARY KEY,
    winner_id       BIGINT,
    winning_bid_id  BIGINT,
    final_price     BIGINT NOT NULL,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);