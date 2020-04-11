SELECT count(*) FROM (
    SELECT count(*) s FROM frequency GROUP BY docid HAVING s > 300
);