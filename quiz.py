from random import*
# 퀴즈1 챕터2

station = "사당"
print(station+"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")
# 퀴즈2  챕터3

oflineDay = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월" + str(oflineDay) + "일로 선정되었습니다.")

# 퀴즈 3 챕터4

website = "http://naver.com"
webAbbreviation = website[7:-4]
web3letters = webAbbreviation[:3]
lenWesite = len(webAbbreviation)
countE = webAbbreviation.count("n")

password = web3letters+str(lenWesite)+str(countE)+"!"

print(password)

# 퀴즈 4 챕터 5
# 내 답안
id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(id_list)
chicken = set(sample(id_list, 1))
id_list = set(id_list)
id_list = id_list-chicken
id_list = list(id_list)
shuffle(id_list)
coffee = sample(id_list, 3)
print(f"-- 당첨자 발표 --\n 치킨 당첨자:{chicken} \n 커피 당첨자:{coffee} \n -- 축하합니다 --")

# 나도 코딩님 답안
users = range(1, 21)  # 1부터 20까지 숫자를 생성
users = list(users)
