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
