SELECT count(*) FROM (
    SELECT * FROM frequency WHERE term = 'law' OR term = 'legal' GROUP BY docid
);