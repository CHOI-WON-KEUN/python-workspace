

import xlsx_util, list_util
import re
import semester as sem
import time_table as t

import importlib, sys


english_supplement_dict = dict(list_util.partition(
re.split(r'\s+', 
'''3103김준현 영미문화탐구
3105서민석 영미문화탐구
3108양지민 영미문화탐구
3112이우진 시사영어
3115현영우 영미문화탐구
3204김태민 시사영어
3207박성준 영미문화탐구
3215황보현 영미문화탐구
3216황성빈 시사영어
3307백우준 영미문화탐구
3406김형운 영미문화탐구
3506김호준 시사영어
3509우상엽 영미문화탐구
3514차지명 영미문화탐구
3515한승범 영미문화탐구
3607오유준 시사영어
3609이재정 시사영어
3612조민재 영미문화탐구
3701구민재 시사영어
3702김준서 시사영어
3707안서영 시사영어
3801김승엽 시사영어
3804김현우 커뮤니케이션
3807손선빈 영미문화탐구
3809윤예람 영미문화탐구
3810이준상 영미문화탐구
3811정승민 시사영어'''), 2))



credit_dict = dict( 
    map(lambda c: ( c[0],int(c[1]) ), list_util.partition(
re.split(r'\s+', 
'''R&EI 4
R&EII 4
객체지향프로그래밍 3
건강과체육I 1
건강과체육II 1
경제학 2
고급물리학I 3
고급물리학II 3
고급생명과학I 3
고급생명과학II 3
고급지구과학 3
고급커뮤니케이션 2
고급화학I 3
고급화학II 3
고전문학 2
과제연구I 4
과제연구II 4
과제연구III 2
과제연구IV 2
과학사 2
국어I 2
국어II 2
기초통계학 3
독서I 1
독서II 1
독서III 1
독서IV 1
디자인 2
매체언어비평 2
문법 2
물리학I 3
물리학II 3
물리학III 4
물리학IV 3
물리학실험I 1
물리학실험II 1
미술I 1
미술II 1
미적분학I 4
미적분학II 4
생명과학I 3
생명과학II 3
생명과학III 3
생명과학IV 3
생명과학실험I 1
생명과학실험II 1
생활미술 2
생활음악 2
생활체육 2
선형대수학 3
세계문화지리 3
세계사 3
수리정보탐구 2
수학I 4
수학II 4
수학III 3
수학IV 4
시사영어 3
여가와체육I 1
여가와체육II 1
영미문화탐구 2
영어I 3
영어II 3
영어III 3
영어독해 3
영어소설 3
영어회화I 1
영어회화II 1
영작문 3
예술사 2
위탁교육 2
융합과학 3
융합과학탐구 3
음악I 1
음악II 1
자료구조 3
자연탐사 2
작문 2
정수론 3
정치경제 3
졸업논문I 2
졸업논문II 2
중국어I 2
중국어II 2
지구과학I 3
지구과학II 3
지구과학III 3
창의융합특강I 2
창의융합특강II 2
창의융합특강III 2
창의융합특강IV 2
창의융합특강V 2
창의융합특강VI 2
창의융합특강VII 2
창의융합특강VIII 2
창의융합특강X 2
창의융합특강XI 2
창의융합특강XII 2
창의융합특강XIII 2
창의융합특강XIV 2
창의융합특강XIX 2
창의융합특강XVIII 2
창의융합특강XX 2
철학 3
커뮤니케이션 2
컴퓨터과학I 2
컴퓨터과학II 2
한국사 3
현대문학 2
화학I 3
화학II 3
화학III 4
화학IV 3
화학실험I 1
화학실험II 1'''
), 2)))




def read_name_semester_subjects_from_xlsx(filename):
    data = xlsx_util.read_xlsx_sheet_into_list(filename)
    output = [ ] 
    sem_pattern = re.compile(r'^\d{4}_\S+')
    for rec in data : 
        if sem_pattern.match(rec[1]):
            output.append(rec)
    return output
    
def shorten_to_neis_entry(subj):
    if subj.startswith("창의융합특강"):
        cut_position = subj.find("/")
        return subj[:cut_position]
    else : 
        return subj

def combine_with_plans( past_triples, next_sem_name_subjects ):
    next_sem_str =  sem.next_semester_prefix[:-1]
    new_triples = [ (c[0], next_sem_str, 
            shorten_to_neis_entry(c[1])) for c in next_sem_name_subjects 
                    if c[0][0] == '3']
    output = list(map(tuple, past_triples))
    output.extend(new_triples)
    output.sort()
    return output

def coursework_list(all_triples, st_name):
    output = [ c[2] for c in all_triples if c[0] in st_name ]
    return output


def test_coursework_on_functions( subject_list, function_list):
    output = True
    for fn in function_list:
        result = fn(subject_list, verbose=True)
        if result is False : 
            output = False
    return output

mandatory_subjects = re.split(r'\s+', 
'''국어I
국어II
독서I
독서II
영어I
영어회화I
영어II
영어회화II
정치경제
세계문화지리
한국사
건강과체육I
건강과체육II
여가와체육I
여가와체육II
음악I
음악II
미술I
미술II
수학I
수학II
수학III
수학IV
물리학I
물리학II
화학I
화학II
생명과학I
생명과학II
지구과학I
지구과학II
컴퓨터과학I
컴퓨터과학II
독서III
독서IV
중국어I
중국어II
철학
세계사
미적분학I
물리학III
화학III
생명과학III
지구과학III
물리학실험I
물리학실험II
화학실험I
화학실험II
생명과학실험I
객체지향프로그래밍''')

mandatory_selects = re.split(r'\s+', 
'''커뮤니케이션
고급커뮤니케이션''')

mandatory_activities = re.split(r'\s+', 
'''R&EI 
R&EII 
과제연구I 
과제연구II
과제연구III
과제연구IV
졸업논문I
졸업논문II'''
)

mandatory_act_selects = re.split(r'\s+', 
'''자연탐사 
위탁교육''')

def contains_all_mandatory_subjects(subject_list, verbose=False):
    output = True
    for subj in mandatory_subjects + mandatory_activities : 
        if subj not in subject_list : 
            output = False
            if verbose : 
                print(f"<{subj}> is missing..")
    if len(list_util.intersect(mandatory_selects, subject_list))==0:
            output = False
            if verbose : 
                print("None of <{}> is found..".format(
                    ','.join(mandatory_selects)))
    if len(list_util.intersect(mandatory_act_selects, subject_list))==0:
            output = False
            if verbose : 
                print("None of <{}> is found..".format(
                    ','.join(mandatory_act_selects)))
    return output


subj_group_req_credits = [ 
[ re.split(r'\s+', '''작문
현대문학
문법
고전문학'''), 6], 
[ re.split(r'\s+', 
'''영어III
영어소설
영작문
시사영어
영어독해'''), 6], 
[ re.split(r'\s+', 
'''생활체육
생활음악
생활미술'''), 2], 
[ re.split(r'\s+', 
'''과학사
수리정보탐구'''), 2], 
[ re.split(r'\s+', 
'''기초통계학
미적분학II'''), 3],
[ re.split(r'\s+', 
'''과학사
수리정보탐구
기초통계학
미적분학II
물리학IV
화학IV
생명과학IV
생명과학실험II 
정수론
선형대수학
고급물리학I
고급물리학II
고급화학I
고급화학II
고급생명과학I
고급생명과학II
고급지구과학
자료구조
창의융합특강I
창의융합특강II
창의융합특강III
창의융합특강IV
창의융합특강V
창의융합특강VI
창의융합특강VII
창의융합특강VIII
창의융합특강X
창의융합특강XI
창의융합특강XII
창의융합특강XIII
창의융합특강XIV
창의융합특강XIX
창의융합특강XVIII
창의융합특강XX'''), 12], 
[ re.split(r'\s+', 
'''매체언어비평
경제학
영미문화탐구
예술사
디자인
작문
현대문학
문법
고전문학
영어III
영어소설
영작문
시사영어
영어독해
생활체육
생활음악
생활미술'''), 4], 
[ re.split(r'\s+', 
'''매체언어비평
경제학
영미문화탐구
예술사
디자인'''), 2], 
[ re.split(r'\s+', 
'''객체지향프로그래밍
건강과체육I
건강과체육II
경제학
고급물리학I
고급물리학II
고급생명과학I
고급생명과학II
고급지구과학
고급커뮤니케이션
고급화학I
고급화학II
고전문학
과학사
국어I
국어II
기초통계학
독서I
독서II
독서III
독서IV
디자인
매체언어비평
문법
물리학I
물리학II
물리학III
물리학IV
물리학실험I
물리학실험II
미술I
미술II
미적분학I
미적분학II
생명과학I
생명과학II
생명과학III
생명과학IV
생명과학실험I
생명과학실험II
생활미술
생활음악
생활체육
선형대수학
세계문화지리
세계사
수리정보탐구
수학I
수학II
수학III
수학IV
시사영어
여가와체육I
여가와체육II
영미문화탐구
영어I
영어II
영어III
영어독해
영어소설
영어회화I
영어회화II
영작문
예술사
융합과학
융합과학탐구
음악I
음악II
자료구조
작문
정수론
정치경제
중국어I
중국어II
지구과학I
지구과학II
지구과학III
창의융합특강I
창의융합특강II
창의융합특강III
창의융합특강IV
창의융합특강V
창의융합특강VI
창의융합특강VII
창의융합특강VIII
창의융합특강X
창의융합특강XI
창의융합특강XII
창의융합특강XIII
창의융합특강XIV
창의융합특강XIX
창의융합특강XVIII
창의융합특강XX
철학
커뮤니케이션
컴퓨터과학I
컴퓨터과학II
한국사
현대문학
화학I
화학II
화학III
화학IV
화학실험I
화학실험II'''), 154]
]

def count_credits_in_group( subject_group, st_subjects):
    completed_subjects = list_util.intersect(subject_group, st_subjects)
    return sum( [credit_dict[subj] for subj in completed_subjects] )



def acquired_all_subject_group_credits(subject_list, verbose=False):
    output = True
    for subj_group, req_credit in subj_group_req_credits :
        acquired_credit = count_credits_in_group(subj_group, subject_list)
        if acquired_credit < req_credit : 
            output = False
            if verbose : 
                print("In group <{}>, only {} is acquired. {} is required.".format( ' '.join(subj_group), acquired_credit, req_credit ))
    return output

if __name__ == "__main__" :
    t.load()
    importlib.reload(t)

    seniors = list_util.prefix_filter("3", t.students)
    all_data = xlsx_util.read_xlsx_sheet_into_list(sys.argv[1])[1:]
    lacking_names = [ ] 
    for st_name in seniors : 
        print(f"Working on <{st_name}>..")
        subj_list = coursework_list(all_data , st_name)
        eng_result = True
        if st_name in english_supplement_dict : 
            eng_subj = english_supplement_dict[st_name]
            print("English supplement {}".format( eng_subj) )
            if eng_subj not in subj_list: 
                print(f"Missing <{eng_subj}>..")
                eng_result = False
            else : 
                subj_list.remove( english_supplement_dict[st_name] )

        result = test_coursework_on_functions( subj_list, 
            [contains_all_mandatory_subjects, 
                acquired_all_subject_group_credits ])
        if result is False or eng_result is False : 
            print(f"Adding <{st_name}> to the list..")
            lacking_names.append(st_name)
    xlsx_util.write_list_into_xlsx("졸업요건_미비목록.xlsx", lacking_names)
        
            

