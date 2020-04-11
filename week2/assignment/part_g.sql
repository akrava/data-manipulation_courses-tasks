SELECT value FROM (
    SELECT a.row_num, b.col_num, SUM(a.value * b.value) as value FROM a, b
        WHERE a.col_num = b.row_num
        GROUP BY a.row_num, b.col_num
) WHERE row_num = 2 AND col_num = 3;