import random

whole_mem = int(input("분반별 전체 인원을 입력하세요.  : "))
squad_num = int(input("조당 배정 인원 수를 입력하세요. : "))
count_num = int(input("구성 횟수를 입력하세요.        : "))

print(f"전체인원 : {whole_mem} 명")
print(f"조당인원 : {squad_num} 명")
print(f"구성회수 : {count_num} 개")

squad_set = set() # 모든 조원의 구성을 담고 있는 집합. 조원의 리스트를 저장함.(중복 조원을 방지하기 위한 용도). 

def make_squad(mem_list): # 조원의 리스트를 구하는 함수. 
    global squad_num
    squad = set()
    
    while len(squad) < squad_num: # 조원의 크기가 조당 인원보다 작다면
        squad.add(random.choice(mem_list)) # 조원을 추가
    return tuple(sorted(squad)) # 정렬된 조원을 튜플로 반환

def construct_squad(mem_list):
    global squad_num, squad_set
    squads = set() # 조원 리스트를 담는 집합
    
    while (len(mem_list) >= squad_num): # 남은 인원이 조당 인원에 못미치면 종료.
        squad = make_squad(mem_list)
        if squad not in squad_set: # 조원 구성 집합에 없는 경우에
            squad_set.add(squad) # 조원 구성 집합에 추가
            mem_list = [x for x in mem_list if x not in squad] # 추가된 인원을 제거
            squads.add(squad)
    
    print(sorted(squads), mem_list)

for _ in range(count_num):
    construct_squad( list(range(1, whole_mem + 1)) )

#print(squad_set)