DO $$
DECLARE
    start_date DATE := date_trunc('month', NOW())::date;
    i INT;
    from_date DATE;
    to_date DATE;
    suffix TEXT;
BEGIN
    FOR i IN 0..11 LOOP
        from_date := start_date + (i || ' month')::interval;
        to_date   := start_date + ((i+1) || ' month')::interval;

        suffix := to_char(from_date, 'YYYY_MM');

        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS bid_%s PARTITION OF bid
             FOR VALUES FROM (%L) TO (%L);',
            suffix, from_date, to_date
        );

        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS wallet_tx_%s PARTITION OF wallet_transactions
             FOR VALUES FROM (%L) TO (%L);',
            suffix, from_date, to_date
        );

        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS payments_%s PARTITION OF payments
             FOR VALUES FROM (%L) TO (%L);',
            suffix, from_date, to_date
        );
    END LOOP;
END $$;