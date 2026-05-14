# dictionary(딕셔너리) : 키와 값의 쌍으로 이루어진 자료형

word_dic={
    "gibeom":"기범",
    "gichan":"기찬",
    "wolfturtle":"늑대거북이",
    "jiwon":"지원"
}
print(word_dic)
print(word_dic["gibeom"]) 


word_dic["gibeom"]="유기범" #딕셔너리의 값 변경
print(word_dic["gibeom"])

word_dic["yuna"]="조유나" #딕셔너리에 새로운 키와 값 추가
print(word_dic["yuna"])

#다음 아이스크림 이름과 가격을 딕셔너리로 구성하라.
#이름 가격 재고
#메로나 1000원 2개
#폴라포 1200원 3개
#빵빠레 1800원 4개

ice_dic={
    "메로나": [1000, 2],
    "폴라포": [1200, 3],
    "빵빠레": [1800, 4]
}           
print(ice_dic)   

print(ice_dic["메로나"][0],"원") #메로나의 가격 출력
print(ice_dic["폴라포"][1],"개") #폴라포의 재고 출력