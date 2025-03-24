groups = ['Hot', 'Seventeen', 'Black Pink', 'NJZ'] # 아이돌 그룹이름
ratings = [1,2,4,3] # 좋아하는 순위

groups_raitings = list(zip(groups,ratings ))
print(groups_raitings)
# zip안에서는 반복문으로 돌고 있음.
#짝이 안맞으면 작은 것 기준으로 돈다.
# 각 인덱스끼리 tuple로 묶어서 zip객체를 반환한다.
cities = ['Suwon', 'Hwasung', 'Incheon' , 'Incheon' ,'Buchoen', 'Seoul']
cities = set(cities)
print(cities)
