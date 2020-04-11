CREATE VIEW IF NOT EXISTS new_frequency as SELECT * FROM frequency
    UNION
    SELECT 'q' as docid, 'washington' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT similarity FROM (
    SELECT d_id docid, sum(sum_similarity) similarity FROM (
        SELECT a.docid, b.docid d_id, a.term, sum(a.count * b.count) sum_similarity
            FROM new_frequency a, new_frequency b
            WHERE a.term = b.term AND a.docid = 'q' AND a.docid != b.docid
            GROUP BY a.docid, b.docid
    ) GROUP BY d_id ORDER BY similarity DESC
) LIMIT 1;