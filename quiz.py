from random import*
from math import*
# # 퀴즈1 챕터2

# station = "사당"
# print(station+"행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station+"행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station+"행 열차가 들어오고 있습니다.")
# # 퀴즈2  챕터3

# oflineDay = randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월" + str(oflineDay) + "일로 선정되었습니다.")

# # 퀴즈 3 챕터4

# website = "http://naver.com"
# webAbbreviation = website[7:-4]
# web3letters = webAbbreviation[:3]
# lenWesite = len(webAbbreviation)
# countE = webAbbreviation.count("n")

# password = web3letters+str(lenWesite)+str(countE)+"!"

# print(password)

# # 퀴즈 4 챕터 5
# # 내 답안
# id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(id_list)
# chicken = set(sample(id_list, 1))
# id_list = set(id_list)
# id_list = id_list-chicken
# id_list = list(id_list)
# shuffle(id_list)
# coffee = sample(id_list, 3)
# print(f"-- 당첨자 발표 --\n 치킨 당첨자:{chicken} \n 커피 당첨자:{coffee} \n -- 축하합니다 --")

# # 나도 코딩님 답안
# users = range(1, 21)  # 1부터 20까지 숫자를 생성
# users = list(users)

# shuffle(users)

# winners = sample(users, 4)  # 4명 중에서 1명은 치킨,3명은 커피

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 :{0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 -- ")

# # 퀴즈 5 챕터 6
# i = 0
# customers = [[i, randrange(5, 51)] for i in range(1, 51)]

# for x in customers:
#     if 5 <= x[1] <= 15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(x[0], x[1]))
#         i += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(x[0], x[1]))
# print("총 탑승 승객 :{0}".format(i))

# #퀴즈 6 챕터 7


def std_weight(height, gender):
    height = height/100
    if gender == "men":
        std = height*height*22
        std = round(std, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height*100, std))
    else:
        std = height*height*21
        std = round(std, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height*100, std))


std_weight(175, "men")
