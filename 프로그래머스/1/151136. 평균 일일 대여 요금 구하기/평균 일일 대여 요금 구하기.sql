-- 코드를 입력하세요
SELECT round(avg(daily_fee), 0)        # 여기서 소수 첫째를 반올림하고 평균 값 출력하기
from car_rental_company_car
where CAR_TYPE = 'SUV'