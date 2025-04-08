-- 코드를 작성해주세요
select count(*) as FISH_COUNT
from fish_info
where LENGTH is null

# where () = null 이건 작동안한다.
# NULL은 비교 불가한 값이기 때문에 =NULL 혹은 !=NULL은 작동하지 않는다.
# 비교하기 우ㅐ해서는 IS NULL 이라는 것을 사용해라.