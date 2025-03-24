def my_zip(l1,l2):
    for i in range(len(l1)):
        r = []
        for i in range(len(l1)):
            r.append((l1[i], l2[i]))
    return r



groups = ['Hot', 'Seventeen', 'Black Pink', 'NJZ']  # 아이돌 그룹이름
ratings = [1, 2, 4, 3]  # 좋아하는 순위
# groups_raitings = list(zip(groups, ratings))
print(my_zip(groups, ratings))