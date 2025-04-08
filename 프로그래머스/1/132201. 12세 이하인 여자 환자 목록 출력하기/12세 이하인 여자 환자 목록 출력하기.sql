-- 코드를 입력하세요
# 공백이라면 ~~라고 출력해는 IFNULL(컬럼명, 대체할 텍스트)를 사용하라.
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 and gend_cd = 'W'
ORDER BY AGE DESC, PT_NAME ASC