-- 코드를 입력하세요
SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, ROUND(AVG(b.REVIEW_SCORE), 2) as SCORE 
from rest_info a
join rest_review b on b.REST_ID = a.REST_ID
GROUP BY A.REST_ID
HAVING a.ADDRESS LIKE '서울%'
order by SCORE desc, a.favorites desc