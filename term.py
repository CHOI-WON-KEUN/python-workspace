# -*- coding: utf-8 -*-

import list_util
import re
import datetime
import random

# 아래 내용 수정
term_str = "2021학년 2학기 기말고사" 

notice_str = term_str + " 시간표 및 고사실 안내" + "\n" + \
            "본인에게 해당되는 고사 및 고사실을 숙지하여 해당 고사실에 10분전 입실완료 바랍니다."

#salt = "Alaska02"
salt = "Wyoming"


# 아래 내용 수정
day_str_dict = { 
1: "제1일 (12월14일 화)", 
2: "제2일 (12월15일 수)", 
3: "제3일 (12월16일 목)", 
4: "제4일 (12월17일 금)", 
5: "제5일 (12월20일 월)",
6: "제6일 (12월21일 화)"
}


# 아래 내용 수정
day_day_dict = { 
1: "화",
2: "수", 
3: "목", 
4: "금", 
5: "월",
6: "화"
}


# 아래 내용 수정
date_day_list = "12월14일(화) 12월15일(수) 12월16일(목) 12월17일(금) 12월20일(월) 12월21일(화)".split() 


#time_periods = [ "1교시 2교시 3교시 4교시 5교시".split(), 
         #"08:30~09:50 10:10~11:00 11:20~13:00 13:30~14:50 15:10~16:00".split()]

#time_periods = [ "1교시 2교시 3교시 4교시 5교시".split(), 
         #"09:20~11:00 11:20~12:10 12:30~13:50 14:10~15:00 15:20~17:00".split()]

time_periods = [ "1교시 2교시 3교시 4교시".split(), 
         "08:30~09:50 10:10~11:00 11:20~13:00 14:00~13:40".split()]


period_starts = [ datetime.datetime(2001,1,1, 8, 30), datetime.datetime(2001,1,1, 10, 10),
                   datetime.datetime(2001,1,1, 11, 20), datetime.datetime(2001,1,1, 14, 0)]


period_lengths = [ 80, 50, 100, 100 ]  


message_template = "다음 URL 에서 자신의 수업시간표를 확인하기 바랍니다. http://url.savano.org/notice/NUMBER_CODE"


prefilled_link = "https://docs.google.com/forms/d/e/1FAIpQLSfvqbXk36Eie1sRBSga8zE0Jb1uQbn3PPcMhO9uTBNwMJ_PXA/viewform?usp=pp_url&entry.925729718=NUMBER&entry.356517579=CODE"

#message = "정수론 수업 Google Classroom 코드는  onnabjp  입니다. 등록한 후 자유게시판에 등록확인 답글을 올려주기 바랍니다." 
#message = "중간고사시간표 제1안을 보냅니다. 수정 후 월요일 오후에 과장, 부장 선생님들께 제2안을 발송할 예정입니다. 송원택 올림. http://url.savano.org/mid01fee"

#message = "안녕하세요. 기말고사 교과 담당 선생님 여러분께 기말고사시간표 제1안을 보냅니다. 오류 또는 수정요청사항이 있는 경우 12월4일까지 제게 알려주시기 바랍니다. 12월5일에 전학년 대상으로 오류여부확인을 할 계획입니다. 송원택 올림.   http://url.savano.org/finalonesheen"

message = "안녕하세요. 서울과학고등학교 교육과정부 송원택입니다. 2021학년 1학기 중 육아시간 사용 등 이유로 수업을 하실 수 없는 요일, 교시가 있다면 1월25일 월요일까지 제게 알려주시기 바랍니다. 송원택 올림." 


# 아래 내용 수정
shuffled_teachers = re.split(r'\s+',
'''김연희t
안민기t
여정필t
김봉준t
이승철t
도현진t
이미영t
조동근t
지우영t
배동일t
조현웅t
홍기만t
이일규t
전효성t
민정아t
임영나t
박은서t
정유선t
박재승t
장광재t
권상운t
송원택t
조미연t
최금뢰t
오미옥t
윤병일t
권용준t
김현호t
박차경t
김근유t
김경훈t
정관영t
조혜영t
이상민t
배종수t
박리원t
민진원t
조현태t
홍석민t
공윤주t
정유정t
조현세t
노예솔t
최병철t
강영미t
이성도t
이슬t
남지애t
황광원t
김유정t
송경수t
유영주t
문세라t
백승용t
박새날t
이경미t
박경희t
조영혜t
이현정t
김홍민t
김현기t
황성현t
김대범t
김상태t
윤상호t
오현선t
김지애t
서여민t
신수진t
성숙경t
박병기t
황성문t
변은지t
허진미t
박다솜t
박효숙t
최원근t''')


# 아래 내용 수정
ordered_exam_subjects = re.split(r'\s+', 
'''국어II
현대문학
고전문학
문법
매체언어비평
정치와법
세계문화지리
한국사
철학
세계사
영어II
영어회화II
커뮤니케이션
고급커뮤니케이션
영어독해
시사영어
영미문화탐구
중국어II
예술사
과학사
수리정보탐구
창의융합특강II/다체론
창의융합특강XIII/분자건축
수학II
수학IV
미적분학I
미적분학II
물리학II
물리학IV
고급물리학II
화학II
화학IV
고급화학I
생명과학II
생명과학IV
고급생명과학I
지구과학I
지구과학II
지구과학III
고급지구과학''')


# 한 교시에 볼 수 있는 강의실 수
max_simul_num = 21 


exam_classrooms = re.split(r'\s+', 
'''수학강의실1
수학강의실2
수학강의실3
수학강의실4
수학강의실5
수학강의실6
수학강의실7
국어강의실1
국어강의실2
국어강의실3
우암공통강의실3
사회강의실3
사회강의실2
사회강의실1
우암공통강의실2
우암공통강의실1
우암공통강의실4
외국어강의실1
외국어강의실2
외국어강의실3
외국어강의실4
외국어강의실5''')

auto_bundle_classroom_dict = {
tuple("국어강의실1 국어강의실2 국어강의실3 사회강의실1 사회강의실2 사회강의실3 우암공통강의실3".split()): 
["국어강의실1 국어강의실2 국어강의실3".split(), "사회강의실1 사회강의실2".split(), "사회강의실3 우암공통강의실3".split()], 
tuple('수학강의실1 수학강의실2 수학강의실3 수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()): 
    ['수학강의실1 수학강의실2 수학강의실3'.split(), '수학강의실4 수학강의실5'.split(), '수학강의실6 수학강의실7'.split()], 
tuple('수학강의실2 수학강의실3 수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()): 
    ['수학강의실2 수학강의실3'.split(), '수학강의실4 수학강의실5'.split(), '수학강의실6 수학강의실7'.split()], 
tuple('우암공통강의실1 우암공통강의실2'.split()):['우암공통강의실1'.split(), '우암공통강의실2'.split() ], 
tuple("사회강의실1 사회강의실2 사회강의실3 우암공통강의실3".split()): 
    ["사회강의실1 사회강의실2".split(), "사회강의실3 우암공통강의실3".split()], 
tuple('수학강의실1'.split()): 
    ['수학강의실1'.split() ],
tuple("외국어강의실1 외국어강의실2 외국어강의실3 외국어강의실4".split()):
    ["외국어강의실1 외국어강의실2 외국어강의실3 외국어강의실4".split()]
}


bundle_classroom_dict = {
tuple('우암공통강의실4'.split()): ['우암공통강의실4'.split()], 
tuple('우암공통강의실1 우암공통강의실2'.split()):['우암공통강의실1'.split(), '우암공통강의실2'.split()],
tuple('수학강의실1 수학강의실2 수학강의실3 수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()): 
    ['수학강의실1 수학강의실2 수학강의실3'.split(), '수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()], 
tuple("국어강의실1 국어강의실2 국어강의실3 사회강의실1 사회강의실2 사회강의실3 우암공통강의실3".split()): 
["국어강의실1 국어강의실2 국어강의실3".split(), "사회강의실1 사회강의실2 사회강의실3 우암공통강의실3".split()], 
tuple("사회강의실1 사회강의실2 사회강의실3 우암공통강의실3".split()): 
["사회강의실1 사회강의실2 사회강의실3 우암공통강의실3".split()], 
tuple("국어강의실1 국어강의실2 국어강의실3 우암공통강의실3".split()): 
["국어강의실1 국어강의실2 국어강의실3 우암공통강의실3".split()], 
tuple('수학강의실3 수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()): 
    ['수학강의실3 수학강의실4'.split(), '수학강의실5 수학강의실6 수학강의실7'.split(),], 
tuple('수학강의실5 수학강의실6 수학강의실7'.split()): 
    ['수학강의실5 수학강의실6 수학강의실7'.split()], 
tuple('수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()): 
    ['수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()], 
tuple('수학강의실2 수학강의실3 수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()): 
    ['수학강의실2 수학강의실3'.split(), '수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split()], 
tuple('수학강의실1 수학강의실2 수학강의실3 수학강의실4'.split()): 
    ['수학강의실1 수학강의실2 수학강의실3 수학강의실4'.split()], 
tuple('외국어강의실1 외국어강의실2 외국어강의실3 외국어강의실4 외국어강의실5'.split()):  
    ['외국어강의실1 외국어강의실2 외국어강의실3 외국어강의실4 외국어강의실5'.split()],
}


bundle_classrooms = [
'우암공통강의실1 우암공통강의실2'.split(),
'수학강의실1 수학강의실2 수학강의실3'.split(),
'수학강의실4 수학강의실5 수학강의실6 수학강의실7'.split(),
'국어강의실1 국어강의실2 국어강의실3'.split(),
'사회강의실1 사회강의실2 사회강의실3 우암공통강의실3'.split(),
'외국어강의실1 외국어강의실2 외국어강의실3 외국어강의실4 외국어강의실5'.split() ]

special_bundle_classrooms = [ 
'수학강의실1 수학강의실2 수학강의실3 수학강의실4'.split()
,'국어강의실1 국어강의실2 국어강의실3 우암공통강의실3'.split(),
'우암공통강의실1 우암공통강의실2'.split(),
]


bundle_classes = [
"생명과학실험II_1 생명과학실험II_2".split()
]

#svB_classes = "영어독해_1 영어독해_2".split()
#svC_classes = "세계사_1 세계사_2 세계사_3 세계사_4 세계사_5".split()

svB_classes = [ ] 
svC_classes = [ ] 
#svC_classes = "영어III_1 영어III_2 영어III_3 수리정보탐구_1 수리정보탐구_2 수리정보탐구_3 고급커뮤니케이션_1 고급커뮤니케이션_2 고급커뮤니케이션_3".split()
#svC_classes = re.split(r'\s+', 
#'''영어독해_1 영어독해_2 영어독해_3 영어독해_4 영어독해_5 영어독해_6 영어독해_7
#컴퓨터과학I_1 컴퓨터과학I_2 컴퓨터과학I_3 컴퓨터과학I_4 컴퓨터과학I_5 컴퓨터과학I_6 컴퓨터과학I_7 컴퓨터과학I_8''')

# 아래 내용 수정
role_dict = dict( list_util.partition( 
re.split(r'\s+', 
'''송원택t 교육과정부장
박은서t 고사
조혜영t 고사
조현웅t 안내방송
문세라t 방송
지우영t 교육과정부기획
최원근t 고사시간표 
백승용t 부장회의 
오현선t 부장회의 
송경수t 부장회의 
김근유t 부장회의 
이일규t 부장회의 
조영혜t 부장회의 
이경미t 부장회의 
최병철t 부장회의 
이성도t 부장회의 
정유선t 부장회의 
민진원t 부장회의 
윤상호t 부장회의'''), 2))


def add_unavailable_slots( update_dict ) : 
    for t_name in update_dict : 
        if t_name in unavailable_teacher_slots_dict : 
            unavailable_teacher_slots_dict[t_name].extend(update_dict[t_name])
        else : 
            unavailable_teacher_slots_dict[t_name] =  update_dict[t_name]


# 아래 내용 수정(교육과정부, 방송, 보건)
unavailable_teacher_slots_dict = {
"송원택t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)], 
"최원근t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"조현웅t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"조혜영t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"박은서t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"지우영t": [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)],  
"문세라t": [(1, 1), (1, 2), (1, 3), (1, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"박효숙t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)]
}

# 아래 내용 수정(시감 불가능한 시간 조사)    # 생활안전부 선생님은 월요일 1교시 빼주기(차량 지도)
add_unavailable_slots( {
"박새날t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"김지애t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"송경수t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4)],
"김대범t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (5, 1)],
"박경희t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4)],
"황성문t": [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4)],
"조동근t": [(5, 1)],
"전효성t": [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)],
"안민기t": [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2)],
"윤병일t": [(4, 2), (5, 2), (5, 3)],
"지우영t": [(4, 2)],
"김상태t": [(4, 2)],
"백승용t": [(4, 2), (4, 3)],
"정유선t": [(4, 3)],
"민진원t": [(4, 3)],
"윤상호t": [(4, 3)],
"이경미t": [(4, 2)],
"이일규t": [(4, 2)],
"최병철t": [(4, 2)],
"김경훈t": [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)],
"권상운t": [(2, 1), (2, 2), (2, 3)],
"최금뢰t": [(5, 2), (5, 3)],
"허진미t": [(4, 1), (4, 2), (4, 3)],
"박리원t": [(5, 1), (5, 2), (5, 3)]
})


# 아래 내용 수정(인정시간, 방송은 첫날과 마지막날, 그 외 공가나 출장 인정)
moderation_dict = {
"문세라t": 50+50
}


# 부장 회의
add_unavailable_slots( {
"백승용t": [(3, 1)],
"송원택t": [(3, 1)],
"오현선t": [(3, 1)],
"송경수t": [(3, 1)],
"조현태t": [(3, 1)],
"이일규t": [(3, 1)],
"조영혜t": [(3, 1)],
"이경미t": [(3, 1)],
"최병철t": [(3, 1)],
"이성도t": [(3, 1)],
"정유선t": [(3, 1)],
"민진원t": [(3, 1)],
"윤상호t": [(3, 1)]
})


# 아래 내용 수정
aa_list = re.split(r'\s+',
'''정유선t 김경훈t 김현기t 남지애t 문세라t 박새날t 오미옥t 배동일t
민진원t 강영미t 박다솜t 박은서t 박재승t 변은지t 허진미t 황성문t
윤상호t 공윤주t 박경희t 이승철t 이현정t 조동근t 최원근t 박병기t'''
)

#======

hide_unavailable_slots =  {
#"변은지t": [  (2,1), (3,1), (4,1),  (6,1) ],
#"이경미t": [ (1,1), (2,1), (3,1), (4,1), (5,1), (6,1)],
#"강영미t": [ (1,1), (2,1), (3,1), (4,1), (5,1), (6,1) ],
}


# 아래 내용 수정
unavailable_sv_teachers_dict = {
"정감독": [ ], 
"부감독": [ ], 
"복도감독": "백승용t 최금뢰t".split() } 


# 아래 내용 수정 (1~4반은 정치와법, 4~8반은 세계문화지리 수정)
avoid_classes_dict = { 
"정유선t": "국어II_1 세계문화지리_1 영어II_1 수학II_1 물리학II_1 화학II_1 생명과학II_1 지구과학I_1".split(),
"김경훈t": "국어II_2 세계문화지리_2 영어II_2 수학II_2 물리학II_2 화학II_2 생명과학II_2 지구과학I_2".split(),
"김현기t": "국어II_3 세계문화지리_3 영어II_3 수학II_3 물리학II_3 화학II_3 생명과학II_3 지구과학I_3".split(),
"남지애t": "국어II_4 세계문화지리_4 영어II_4 수학II_4 물리학II_4 화학II_4 생명과학II_4 지구과학I_4".split(),
"문세라t": "국어II_5 정치와법_1 영어II_5 수학II_5 물리학II_5 화학II_5 생명과학II_5 지구과학I_5".split(),
"박새날t": "국어II_6 정치와법_2 영어II_6 수학II_6 물리학II_6 화학II_6 생명과학II_6 지구과학I_6".split(),
"오미옥t": "국어II_7 정치와법_3 영어II_7 수학II_7 물리학II_7 화학II_7 생명과학II_7 지구과학I_7".split(),
"배동일t": "국어II_8 정치와법_4 영어II_8 수학II_8 물리학II_8 화학II_8 생명과학II_8 지구과학I_8".split()
}


# 아래 내용 수정
first_year_advisors = [ "정유선t", "김경훈t", "김현기t", "남지애t", "문세라t", "박새날t", "오미옥t", "배동일t"]
second_year_advisors = "민진원t 강영미t 박다솜t 박은서t 박재승t 변은지t 허진미t 황성문t".split()
third_year_advisors = "윤상호t 공윤주t 박경희t 이승철t 이현정t 조동근t 최원근t 박병기t".split()


# 아래 내용 수정
auto_subjects = re.split(r'\s+',
'''수리정보탐구
창의융합특강II/다체론
미적분학II
물리학II
물리학IV
고급물리학II
화학II
고급화학I
고급생명과학I
지구과학I
지구과학II''')


# 아래 내용 수정        # 추상대수학I의 경우 1분반 수업, 조현웅 선생님인데 부감을 넣어도 되나요?
preassigned_pairs = dict(map( lambda x: ( (x[1], x[2]), x[0] ), 
list_util.partition( re.split(r'\s+',
'''신수진t 고급커뮤니케이션_1 정감독
오현선t 과학사_1 정감독
오현선t 과학사_2 정감독
장광재t 수리정보탐구_1 정감독
도현진t 창의융합특강II/다체론_1 정감독
조미연t 창의융합특강VIII/분자건축_1 부감독
윤상호t 미적분학II_1 정감독
이현정t 고급물리학II_1 정감독
이현정t 고급물리학II_2 정감독
조미연t 화학IV_1 부감독
김근유t 고급화학I_1 정감독
민정아t 생명과학IV_1 부감독
배종수t 고급생명과학I_1 정감독
이상민t 고급지구과학_1 부감독'''), 3)))


shorthand_dict = dict( list_util.partition( 
re.split(r'\s+',
'''고급화학I 고화I
고급화학II 고화II
생명과학IV 생과IV
고급생명과학II 고생II 
고급생명과학I 고생I 
고급물리학II 고물II
창의융합특강XI/일반상대성이론 상대론
창의융합특강II/다체론 다체론
창의융합특강I/위상수학과곡면 위상
수리정보탐구 수정탐
영어독해 영독
고급지구과학 고지
창의융합특강VIII/분자건축 분자
창의융합특강VI/고체물리 고체
창의융합특강XII/데이터와인공지능 지능
창의융합특강XI/양자계산 양자계산'''), 2))

def shorten_by_dict(subj) : 
    if subj in shorthand_dict : 
        return shorthand_dict[subj]
    else : 
        return subj


flu_classroom_dict = {
#((2, 2), "중국어I_8") : "화학강의실1", 
#((1, 1), "수학III_10") : "화학강의실1", 
#((3, 3), "지구과학I_10") : "화학강의실1", 
#((5, 3), "기초통계학_10") : "화학강의실1", 
#((2, 3), "물리학III_9") : "화학강의실1", 
#((4, 3), "화학III_9") : "화학강의실1", 
#((1, 4), "한국사_5") : "화학강의실1"
}

flu_supervisor_dict = { 
#((2, 2), "중국어I_8", "정감독") : None,
#((1, 1), "수학III_10", "정감독") : None,
#((1, 4), "한국사_5", "정감독") : None
}


temp_added_time_dict = { 
#"김지애t": -(60 * 5), 
#"조영혜t": -(60 * 5),
"김연희t": 500,
}


# 아래 내용 수정
accumulated_time_dict = dict( map( lambda x: (x[0], int(x[1])), 
list_util.partition(re.split(r'\s+',
'''강영미t 785
남지애t 800
박경희t 785
임영나t 775
조영혜t 780
조혜영t 0
김경훈t 780
조동근t 790
허진미t 785
황광원t 790
김유정t 815
김지애t 775
김현기t 825
노예솔t 790
민진원t 790
박차경t 875
송원택t 0
오미옥t 785
유영주t 795
윤상호t 795
이승철t 785
조현웅t 80
최병철t 800
홍석민t 800
황성문t 790
권상운t 795
권용준t 795
김상태t 790
도현진t 775
문세라t 790
박재승t 855
배동일t 785
안민기t 820
이현정t 775
전효성t 785
조현세t 795
김근유t 800
김현호t 810
박새날t 555
박은서t 0
성숙경t 915
정관영t 800
조미연t 775
지우영t 545
최원근t 65
김봉준t 895
민정아t 800
배종수t 785
백승용t 780
서여민t 830
오현선t 790
이슬t 865
이일규t 780
여정필t 790
윤병일t 775
이상민t 790
이성도t 780
조현태t 780
황성현t 800
김연희t 335
박다솜t 905
박병기t 795
이경미t 800
장광재t 795
공윤주t 790
김홍민t 845
박리원t 790
신수진t 785
이미영t 800
정유선t 800
홍기만t 790
김대범t 800
변은지t 800
송경수t 780
정유정t 805
박효숙t 0
최금뢰t 780'''), 2)))


pair_weights = { 
("미적분학I", "수학IV"): 218,
("물리학IV", "수학IV"): 96,
("수학IV", "지구과학II"): 91,
("물리학IV", "미적분학I"): 87,
("물리학II", "수학II"): 65,
("객체지향프로그래밍", "지구과학III"): 57,
("미적분학I", "지구과학II"): 45,
("객체지향프로그래밍", "수학IV"): 40,
("생명과학II", "융합과학"): 36,
("물리학II", "화학II"): 33,
("수학II", "컴퓨터과학II"): 30,
("세계사", "지구과학III"): 28,
("생명과학II", "화학II"): 27,
("세계사", "예술사"): 27,
("수학IV", "중국어II"): 27,
("생명과학II", "컴퓨터과학II"): 26,
("컴퓨터과학II", "화학II"): 25,
("물리학II", "컴퓨터과학II"): 22,
("수학II", "화학II"): 22,
("중국어II", "한국사"): 22,
("미적분학I", "중국어II"): 20,
("객체지향프로그래밍", "미적분학I"): 19,
("물리학IV", "지구과학II"): 19,
("융합과학", "화학II"): 19,
("객체지향프로그래밍", "세계사"): 18,
("생명과학II", "영어II"): 18,
("중국어II", "지구과학II"): 16,
("국어II", "수학II"): 15,
("생명과학IV", "지구과학II"): 15,
("고전문학", "철학"): 14,
("수학IV", "화학IV"): 14,
("융합과학", "컴퓨터과학II"): 14,
("지구과학II", "한국사"): 14,
("고급물리학I", "수학IV"): 13,
("객체지향프로그래밍", "고급화학II"): 12,
("고급물리학I", "물리학IV"): 12,
("고급물리학I", "미적분학I"): 12,
("미적분학II", "지구과학III"): 12,
("고급물리학II", "미적분학I"): 11,
("고급생명과학I", "생명과학IV"): 11,
("고급화학I", "수학IV"): 11,
("고급화학II", "지구과학III"): 11,
("문법", "영미문화탐구"): 11,
("물리학IV", "중국어II"): 11,
("고급물리학II", "수학IV"): 10,
("고급화학I", "화학IV"): 10,
("세계사", "시사영어"): 10,
("시사영어", "현대문학"): 10,
("객체지향프로그래밍", "지구과학II"): 9,
("고전문학", "지구과학II"): 9,
("과학사", "한국사"): 9,
("물리학II", "생명과학II"): 9,
("물리학II", "영어II"): 9,
("생명과학II", "정치경제"): 9,
("수학IV", "철학"): 9,
("지구과학II", "화학IV"): 9,
("고전문학", "세계사"): 8,
("미적분학I", "철학"): 8,
("미적분학II", "세계사"): 8,
("세계사", "지구과학II"): 8,
("수학II", "영어II"): 8,
("시사영어", "지구과학III"): 8,
("고급생명과학I", "지구과학II"): 7,
("고전문학", "과학사"): 7,
("객체지향프로그래밍", "문법"): 6,
("객체지향프로그래밍", "미적분학II"): 6,
("객체지향프로그래밍", "시사영어"): 6,
("고급물리학I", "중국어II"): 6,
("고급물리학II", "고급화학II"): 6,
("고급화학I", "미적분학II"): 6,
("고급화학II", "미적분학II"): 6,
("고급화학II", "세계사"): 6,
("고전문학", "영미문화탐구"): 6,
("고전문학", "지구과학III"): 6,
("미적분학I", "화학IV"): 6,
("수학II", "융합과학"): 6,
("시사영어", "예술사"): 6,
("영어II", "화학II"): 6,
("예술사", "지구과학II"): 6,
("융합과학", "정치경제"): 6,
("중국어II", "철학"): 6,
("중국어II", "커뮤니케이션"): 6,
("객체지향프로그래밍", "예술사"): 5,
("객체지향프로그래밍", "현대문학"): 5,
("고급물리학II", "지구과학II"): 5,
("고급화학II", "고전문학"): 5,
("고급화학II", "지구과학II"): 5,
("국어II", "물리학II"): 5,
("문법", "지구과학III"): 5,
("물리학IV", "미적분학II"): 5,
("생명과학II", "세계문화지리"): 5,
("세계사", "현대문학"): 5,
("시사영어", "영어독해"): 5,
("영어II", "융합과학"): 5,
("지구과학II", "철학"): 5,
("객체지향프로그래밍", "한국사"): 4,
("고급물리학I", "지구과학II"): 4,
("고전문학", "수학IV"): 4,
("고전문학", "화학IV"): 4,
("국어II", "영어II"): 4,
("국어II", "융합과학"): 4,
("문법", "세계사"): 4,
("미적분학II", "수학IV"): 4,
("미적분학II", "예술사"): 4,
("수학II", "정치경제"): 4,
("수학IV", "시사영어"): 4,
("영미문화탐구", "지구과학II"): 4,
("지구과학III", "현대문학"): 4,
("철학", "커뮤니케이션"): 4,
("고전문학", "미적분학II"): 3,
("과학사", "세계사"): 3,
("과학사", "시사영어"): 3,
("과학사", "지구과학II"): 3,
("문법", "지구과학II"): 3,
("물리학II", "수학IV"): 3,
("생명과학IV", "중국어II"): 3,
("정치경제", "화학II"): 3,
("고급생명과학I", "수학IV"): 2,
("고급화학I", "지구과학II"): 2,
("과학사", "지구과학III"): 2,
("국어II", "세계문화지리"): 2,
("물리학II", "융합과학"): 2,
("미적분학I", "영미문화탐구"): 2,
("미적분학II", "지구과학II"): 2,
("미적분학II", "현대문학"): 2,
("수학IV", "한국사"): 2 
}

first_third_avoid_teachers = re.split(r'\s+',
""
)


consec_avoid_teachers = re.split(r'\s+',
"")


avoid_teacher_pairs = list_util.partition( re.split(r'\s+',
'''김근유t 박새날t 
김근유t 오현선t
지우영t 오현선t
이경미t 오현선t
조미연t 오현선t'''), 2)