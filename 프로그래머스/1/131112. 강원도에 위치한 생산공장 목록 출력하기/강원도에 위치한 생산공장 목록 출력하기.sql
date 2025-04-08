-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
# 특정 글자가 있는 것을 가져와야 한다.\
# 이떄는 와일드카드(%)와 LIKE를 사용한다.
WHERE ADDRESS LIKE "%강원도%" 
ORDER BY FACTORY_ID ASC