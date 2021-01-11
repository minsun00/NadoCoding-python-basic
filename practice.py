# ------------------------------------저의 복습 및 나중에 까먹을때 볼려고 적은 것입니다---------------------------------------------


# -----------------------------------------------------챕터 4-5 탈출문자----------------------------------------------------------

# \n 줄바꿈

# print("백문이 불여일견 \n 백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.

# print("저는 '나도코딩' 입니다.")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다.")

# \\:문장 내에서 \

# print("C:\\users\\Nacocoding\\Desktop\\pythonWorkspace>")

# \r : 커서를 맨 앞으로 이동

# print("Red Apple\rPine")

# \b :백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

# -----------------------------------------------------챕터 5-1 리스트--------------------------------------------------------------
# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# 위 방법보다 아래의 방법이 효율적

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# # 조세호씨가 몇 번쨰 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")  # append 맨뒤에 더함
# print(subway)

# # 정형돈씨를 유재석 /조세호 사이에 태워봄
# subway.insert(1, "정형돈")  # .insert 1에 자리에 값넘
# print(subway)

# # 지하철에서 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())  # .pop() 아무것도 안 넣을 시 맨 뒤에 값 뺌
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능하다
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형과도 함께 사용가능하다
# num_list = [5, 2, 4, 3, 1]
# mix_list = ["조세호", 20, True]  # true 쓸때 앞글자 대문자로 True
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)  # 하나의 리스트로 합칠수 있다
# print(num_list)
# print(mix_list)

# #-----------------------------------------------------챕터 5-2 사전 ------------------------------------------------------------

# cabinet = {3: "유재석", 100: "김태호"}  # 캐비넷 열쇠키 3번 유재석씨 100번 김태호씨 가 소유중
# # print(cabinet[3]) #방법 1
# # print(cabinet[100])

# # print(cabinet.get(3)) # 방법 2
# # print(cabinet[5]) # 대괄호 [] 사용하면 없는거 가져올때 오류 나옴
# # print(cabinet(5)) # 소괄호 () 사용하면 없는거 가져올떄 none 나옴

# print(cabinet.get(5, "사용가능"))  # 약간 응용 느낌인 듯 get 함수 없는 값 넣으면 뒤에 거 너 집 있는 값이면 그 값 반환함

# print(3 in cabinet) #True #어떤 값이 있나? 확인하는법
# print(5 in cabinet) #False

# cabinet = {"A-3": "유재석", "B-100": "김태호"}  # 정수값만이 아니라 string값도 가능
# print(cabinet["A-3"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key,value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# # ------------------------------------------------------------챕터 5-3 튜플 -----------------------------------------------------

# !!!튜플은 리스트와 같으나 다만 변경및 추가 불가능 but 리스트보다 속도가 빠름 그래서 변경되지 않는 종목 사용시 좋음 !!!
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스") #오류!! 튜플은 추가 및 변경 x

# 튜플 활용

# name = "김종국"
# age = 20
# hobby = "코딩"

# #아래처럼 활용 가능
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# ----------------------------------------------챕터 5-4 세트set(집합) 중복 안됨,순서 없음----------------------------------------
# my_set = {1, 2, 3, 3, 3}  # 사전과 비슷하게 중괄호 사용하나 여기서는 그냥 값만 나열하면 됨
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 java 와 python 을 모두 할 수 있는 개발자
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))  # 값 정렬 순서 안중요

# # 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java 를 까먹음
# java.remove("김태호")
# print(java)

# # -----------------------------------------------------챕터 5-5 자료구조의 변경-------------------------------------------------------
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# # --------------------------------------------------------챕터 6-1 if----------------------------------------------------------------
# weather = input("오늘 날씨는 어떄요?") #input은 항상 string 값으로 반환함
# if weather=="비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요?"))
# if 30<= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10<=temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0<=temp <10:
#     print("너무 추워요. 나가지 마세요")

# # --------------------------------------------------------챕터 6-2 for 반복문1--------------------------------------------------------------
# for Wating_no in range(1, 6):  # 1, 2, 3, 4, 5
#     print("대기번호:{0}".format(Wating_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0},커피가 준비되었습니다.".format(customer))
# # --------------------------------------------------------챕터 6-3 while 반복문2----------------------------------------------------------------
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0},커피가 준비 되었습니다.{1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# 무한반복 컨트롤 c 누르면 멈춤
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0},커피가 준비 되었습니다.{1} 번 남았어요.".format(customer, index))
#     index+=1

# customer = "토르"
# person = "unknown"

# while person != customer:
#     print("{0},커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# # --------------------------------------------------------챕터 6-4 continue와 break----------------------------------------------------------------
# absent = [2, 5]  # 결석
# no_book = {7}  # 책을 깜빡함
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
#         break
#     print("{0},책을 읽어봐".format(student))

# # --------------------------------------------------------챕터 6-5 한줄 for문----------------------------------------------------------------
# # 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102 ,103 ,104.
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i)for i in students]
# print(students)

# # 학생 이름을 대문자로 반환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)
# # --------------------------------------------------------챕터 7-1 함수----------------------------------------------------------------
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()
# # --------------------------------------------------------챕터 7-2 전달값 반환값----------------------------------------------------------------
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):  # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
#     return balance + money


# def withdraw(balance, money):  # 출금
#     if balance >= money:  # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance


# def withdraw_night(balance, money):  # 저녁에 출금
#     commission = 100  # 수수료 100원
#     return commission, balance - money - commission


# balance = 0  # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# # --------------------------------------------------------챕터 7-3 기본값----------------------------------------------------------------
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업 이런 상황에서 기본옵션 사용됨
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


# profile("유재석")
# profile("김태호")
# # --------------------------------------------------------챕터 7-4 키워드 값----------------------------------------------------------------
# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20) # 이렇게 하면 순서 뒤바뀌어도 입력 잘됨
# # --------------------------------------------------------챕터 7-5 가변인자----------------------------------------------------------------
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}".format(name, age),
#           end=" ")  # end 이렇게 쓰면 출력시 줄바꿈 안함
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "python", "Java", "c", "c++", "c#")

# profile("김태호", 25, "kotlin", "swift", "", "", "") # 위처럼하면 값 너을꺼 없을떄 마다 "" 해줘야 해서 비효율

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "python", "Java", "c", "c++", "c#", "JavScript")
# profile("김태호", 25, "kotlin", "swift")

# # --------------------------------------------------------챕터 7-6 지역변수와 전역변수----------------------------------------------------------------
# gun = 10

# def checkpoint(soldiers):  # 경계근무
#     # gun =20  #지역변수
#     global gun  # 전역 공간에 있는 gun 사용  !!!일반적으로 전역 변수 잘 안씀  !!!
#     gun = gun-soldiers
#     print("[함수내] 남은 총:{0}".format(gun))


# def checkpoint_ret(gun, soldiers):  #보통은 아래와 같이 사용
#     gun = gun - soldiers
#     print("[함수내] 남은 총:{0}".format(gun))
#     return gun


# print("전체 총:{0}".format(gun))
# checkpoint(2)  # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
# # --------------------------------------------------------챕터 8-1 표준입출력----------------------------------------------------------------
# print("Python", "Java")  # Python Java
# print("Python", "Java", sep=",")  # Python,Java
# print("Python", "Java", "Javscript", sep=",") # 2개 이상도 ok Python,Java,Javscript
# print("Python", "Java")  # Python Java \t
# print("Python", "Java", end="?")  # Python Java?

# import sys
# print("Python", "Java", file=sys.stdout)  # 표준 출력
# print("Python", "Java", file=sys.stderr)  # 표준 에러

# #시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# # 은행 대기 순번표
# # 001,002,003...
# for num in range(1, 21):
#     print("대기번호 :"+str(num).zfill(3))  # 3개 공간 확보하고 나머지부분 0으로 채워라

# answer = input("아무 값이나 입력하세요 :")  # string 값으로만 반환함
# print("입력하신 값은 " + answer + "입니다")
# # --------------------------------------------------------챕터 8-2 다양한 출력포멧----------------------------------------------------------------
# #빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 떄는 +로 표시, 음수일 떈 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(1000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(10000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))
# # --------------------------------------------------------챕터 8-3 파일 입출력----------------------------------------------------------------
# score_file = open("score.txt", "w", encoding="utf8") # w write 쓰기목적 utf8 한글쓸때 이상하게 안나오게해줌
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")  # a append 이미 있는 파일에 덮어쓰다
# score_file.write("과학 : 80")  # print가 아니라 따로 줄바꿈 x
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8") #r read 파일을 읽는다
# print(score_file.read()) #파일에 있는 모든내용 불러옴
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")  # 파일이 몇줄일지 모를때 1
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")  # 파일이 몇줄일지 모를떄 2
# lines = score_file.readlines()  # list 향태로 저장 readline readlines 구별 잘하자
# for line in lines:
#     print(line)

# score_file.close()
# # --------------------------------------------------------챕터 8-4 pickle ----------------------------------------------------------------
# # 피클은 프로그램상에 우리가 사용하고 있는 데이터를  파일로 저장함 파일을 줌 받은사람은 피클을 이용해서 다시 사용함
# import pickle
# wb write binary pickle를 쓰기위해서는 항상 바이너리 파일을 써야한다
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30,  "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")  # read binary
# profile = pickle.load(profile_file)  # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()
# # --------------------------------------------------------챕터 8-5 with----------------------------------------------------------------
# import pickle

# with를 사용시 편안하게 파일을 만들고 읽을 수 있음

# with open("profile.pickle","rb") as profile_file:
#   print(pickle.load(profile_file+))

# with open("study.text", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.text", "r", encoding="utf8") as study_file:
#     print(study_file.read())
