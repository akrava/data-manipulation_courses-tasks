CREATE VIEW IF NOT EXISTS crude AS SELECT * from frequency where docid = '10080_txt_crude';
CREATE VIEW IF NOT EXISTS earn AS SELECT * from frequency where docid = '17035_txt_earn';

SELECT sum(crude.count * earn.count) FROM crude, earn
    WHERE crude.term = earn.term
    GROUP BY crude.docid, earn.docid;