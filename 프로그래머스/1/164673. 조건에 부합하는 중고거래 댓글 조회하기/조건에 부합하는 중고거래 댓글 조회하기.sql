-- 코드를 입력하세요
SELECT a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS, date_format(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from used_goods_board a
join used_goods_reply b on b.BOARD_ID = a.BOARD_ID
where YEAR(a.CREATED_DATE) = '2022' and MONTH(a.CREATED_DATE) = '10'
order by b.CREATED_DATE asc, a.TITLE asc