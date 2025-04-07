-- 코드를 입력하세요
SELECT FLAVOR
from FIRST_HALF
where flavor in 
      (select flavor
       from ICECREAM_INFO
       where INGREDIENT_TYPE = 'fruit_based'
        )
 and total_order > 3000