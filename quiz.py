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