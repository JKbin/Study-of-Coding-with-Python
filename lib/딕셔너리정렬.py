score_dict = {
    'sam':23,
    'john':30,
    'mathew':29,
    'riti':27,
    'aadi':31,
    'sachin':28
}



# 점수별로 정렬
new_dict = sorted(score_dict.items(),key=lambda x:x[1],reverse=True)
print(new_dict)

# 이름으로 정렬
name_dict = sorted(score_dict,key=lambda x:x[1],reverse=True)
print(name_dict)
