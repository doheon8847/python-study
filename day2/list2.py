movie_list=["아바타","왕사남","살목지","극한직업"]
print(movie_list)
#insert는 리스트의 원하는 위치에 요소를 추가
movie_list.insert(1,"범죄도시")
print(movie_list)
#append는 리스트의 맨 뒤에 요소를 추가
movie_list.append("슈퍼맨")
print(movie_list)
#remove는 요소의 이름으로 삭제
movie_list.remove("살목지")
print(movie_list)

#del은 인덱스 번호로 삭제
del movie_list[2]
print(movie_list)

x=10
print(x)
del x
# print(x)

print(len(movie_list)) #len은 리스트의 길이, 즉 요소의 개수를 반환하는 함수


a= [1,2,3]
print(sum(a)) #sum은 리스트의 모든 요소의 합을 반환하는 함수

# 90,50,80,70,55
# 평균 구하세요
# sum, len 이용
a = [90,50,80,70,55]
avg = sum(a)/len(a) 
print(avg)