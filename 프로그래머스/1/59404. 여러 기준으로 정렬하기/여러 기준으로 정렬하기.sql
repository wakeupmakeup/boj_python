-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
GROUP BY NAME, DATETIME
ORDER BY NAME ASC, DATETIME DESC