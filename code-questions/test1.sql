

-- Returns a table consisting of three columns:
-- country, export, and import
-- which contain the sums of values of the exported imported goods for every country
-- obs: left join ensures that countries that have 0 trades are shown
-- obs: coalesce ensures null sums are zero

SELECT c.country, COALESCE(SUM(sell_trades.value), 0) AS import, COALESCE(SUM(buy_trades.value), 0) AS import
FROM companies c
LEFT JOIN trades sell_trades ON c.name = sell_trades.seller
LEFT JOIN trades buy_trades ON c.name = buy_trades.buyer
GROUP BY c.country
ORDER BY c.country;


-- Example test:   (example test)
-- Returned value: 
-- +--------------------+-----+-----+
-- |          Mathlands |  30 | 180 |
-- |        Nothingland |   0 |   0 |
-- | Underwater Kingdom |  90 |   0 |
-- |         Wonderland | 100 |  40 |
-- +--------------------+-----+-----+
-- OK

-- Your test case: 
-- insert into companies values ('Alice s.p.', 'Wonderland');
-- insert into companies values ('Y-zap', 'Wonderland');
-- insert into companies values ('Absolute', 'Mathlands');
-- insert into companies values ('Arcus t.g.', 'Mathlands');
-- insert into companies values ('Lil Mermaid', 'Underwater Kingdom');
-- insert into companies values ('None at all', 'Nothingland');
-- insert into trades values (20121107, 'Lil Mermaid', 'Alice s.p.', 10);
-- insert into trades values (20123112, 'Arcus t.g.', 'Y-zap', 30);
-- insert into trades values (20120125, 'Alice s.p.', 'Arcus t.g.', 100);
-- insert into trades values (20120216, 'Lil Mermaid', 'Absolute', 30);
-- insert into trades values (20120217, 'Lil Mermaid', 'Absolute', 50);

-- Returned value: 
-- +--------------------+-----+-----+
-- |          Mathlands |  30 | 180 |
-- |        Nothingland |   0 |   0 |
-- | Underwater Kingdom |  90 |   0 |
-- |         Wonderland | 100 |  40 |
-- +--------------------+-----+-----+

-- Your code is syntactically correct and works properly on the example test.