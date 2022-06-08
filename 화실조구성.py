import random

whole_mem = int(input("분반별 전체 인원을 입력하세요. : "))
squad_num = int(input("1조당 배정 인원 수를 입력하세요. : "))

whole_list = list(range(1, whole_mem + 1))      # 사람 번호는 1번부터 시작
print(f"전체인원 : {whole_mem}명")
print(f"조당인원 : {squad_num}명")

for i in range(whole_mem//squad_num):
    squad = []
    squad.sort()

    while len(squad) < squad_num:
        student = random.choice(whole_list)

        if student not in squad:
            squad.append(student)
            whole_list.remove(student)
    print(chr(ord("@")+(i+1)), "조 : ", squad)

if len(whole_list) != 0:
    print(f"남은인원 : {whole_list}")