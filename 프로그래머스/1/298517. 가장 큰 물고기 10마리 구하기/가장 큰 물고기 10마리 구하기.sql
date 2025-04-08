-- 코드를 작성해주세요
select ID, LENGTH
from fish_info
where length > 10
order by length desc, ID asc
limit 10
