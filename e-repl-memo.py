
# 준비단계 


# <midterm_exam_subjects.xlsx> 에 시험과목정보 입력 ( 교과명, 시간(분) )

# 과목별 시험시간(분) 로드 
>>> e.make_exam_subjects("midterm_exam_subjects.xlsx")
>>> l.show_dict(e.subject_minutes_dict)
>>> l.npr(e.exam_subjects)
>>> e.save()

# 동시시험 가능 과목 목록 만들기  e.stackable_subjects_dict
>>> e.make_stackable_subjects_dict()
>>> e.save()

# 시험교시 생성 e.slot_minutes_dict
>>> e.make_minutes_dict(5)

# 고사시간표 초기화 initialize slot_subject_list_dict 
>>> e.initialize_slot_subjects()
>>> e.show_assigned_subjects(); e.show_assigned_minutes(); e.show_overloading()

#================

# <term.py> 정보 업데이트 
# In term.py

# 시험 일정 정보 입력 
# term_str 
# notice_str
# day_str_dict
# day_day_dict
# date_day_list
# time_periods 
# period_starts 
# period_lengths 

# 감독교사 명단 입력
# shuffled_teachers  random.shuffle  t.teachers + ["최금뢰t"] - ["김지우t"]

# 시험과목 목록 
# ordered_exam_subjects  sorted(e.exam_subjects)

# 감독관 비고란 정보 업데이트 
# role_dict   (조현웅t 방송안내) 

# 시험감독 불가 교시 지정 
# unavailable_teacher_slots_dict

# 감독시간 인정 시간(분) 입력 
# moderation_dict

# 담임 명단 입력 
# aa_list 

# 복도감독 회피 명단 입력 
# unavailable_sv_teachers_dict 

# 1학년 담임 감독 회피 과목 지정 
# avoid_classes_dict

# 자율감독 시험 과목 입력 
# auto_subjects

# 감독 역할  분반 사전 지정 (모든 부임 교사는 첫날 80분 시험 부감독에 배정 )
# preassigned_pairs

# 과목 줄임말 지정 
# shorthand_dict

# 시험감독 미리하기 지정 
# temp_added_time_dict

# 연간 누적 감독 시간 입력  1학기 중간고사 시작 전 전 교사 0 분 
# accumulated_time_dict

# 연속 감독 회피 교사 입력 
# consec_avoid_teachers

# 정부감독 회피 쌍 입력 
# avoid_teacher_pairs

#=============

# 분반 수 저장  e.subject_clnum_dict
>>> e.make_subject_clnum_dict()


# 미배정 과목 확인 후 배정  반복 
>>> e.remaining_subjects()
>>> e.available_slots(_[16])
>>> e.assign_slot_subject(* _[0])
>>> e.show_assigned_subjects(); e.show_assigned_minutes(); e.show_overloading()

# 학생 1일 시험 부담 확인 
>>> e.show_overloading()

>>> e.overloading_students(3)





e.show_assigned_subjects(); e.show_assigned_minutes(); e.show_overloading()

e.export_exam_table_xlsx("ttt03.xlsx", " (제1안)")



# 고사실 배정 초기화 e.classroom_dict
>>> e.initialize_classroom_dict()

# 자율감독 시험과목 입력 term.auto_subjects 

# 감독관 배정 초기화 및 사전 배정 
>>> e.initialize_supervisor_dict(); e.assign_preassigned() 


# 고사실 감독관 화면 출력 
>>> e.show_classroom_assignment()

# 고사실 배정 
>>> e.assign_slot_classrooms( (1,1),  l.firsts(x.read_xlsx_sheet_into_list("classrooms.xlsx")))

# 고사실 배정표 출력 
>>> e.export_classroom_assignment_xlsx("ttt01.xlsx")

e.initialize_supervisor_dict(special_room=True); e.assign_preassigned() 

for k in range(180) : e.assign_first_teacher( e.remaining_positions( [e.svB] )[0] )



for k in range(240) : e.assign_first_teacher(e.remaining_positions( [e.svC])[0]);

for k in range(240) : e.assign_first_teacher( [c for c in e.remaining_positions([e.svA]) if t.subject_name_of(c[1]) not in term.auto_subjects ] [0]);

for k in range(240) : e.assign_first_teacher( [c for c in e.remaining_positions([e.svB]) if t.subject_name_of(c[1]) not in term.auto_subjects ] [0]);

for k in range(240) : e.assign_first_teacher(e.remaining_positions( [e.svA])[0]);

for k in range(240) : e.assign_first_teacher(e.remaining_positions( [e.svB])[0]);







for k in range(240) : e.assign_first_teacher(e.remaining_positions( [e.svA])[0])

for k in range(240) : e.assign_first_teacher( [c for c in e.remaining_positions([e.svA]) if t.subject_name_of(c[1]) not in term.auto_subjects ] [0])

e.show_teacher_minutes()


for a in sorted(term.shuffled_teachers, key = e.count_minutes) : print e.schedule_str(a)

for a in sorted(term.shuffled_teachers, key = lambda x:e.count_minutes(x,False)) : print e.schedule_str(a, True)
for a in sorted(term.shuffled_teachers, key = lambda x:e.count_minutes(x,False, raw=True )) : print e.schedule_str(a, False, raw=True)

for a in sorted(term.shuffled_teachers, key = lambda x:e.count_minutes(x,moderation=True, raw=False, accumulation=True )) : print( e.schedule_str(a, moderation=True, raw=False))


e.assign_first_teacher(e.remaining_positions( [e.svA, e.svB, e.svC])[0], avoid_serial=False)

e.assign_first_teacher(e.remaining_positions( [e.svA, e.svB, e.svC])[0], avoid_serial=True)

for i in range(1,7): e.export_assignment_by_day_xlsx(i)

e.relieve_name_slot("t", (1,1))

for a in sorted( e.available_teachers(e.remaining_positions()[0], top=12) , key = lambda x:e.count_minutes(x,moderation=True, raw=False, accumulation=True )) : print e.schedule_str(a, moderation=True, raw=False)

e.assign_teacher_at("t", e.remaining_positions()[0])


bbb = l.cycled(aaa, count=4, start=3,end=11)

e.export_big_supervisor_table("ttt01.xlsx", svD = False) 

e.assign_firsts(idx=0)



for subj in t.subjects :
    aaa = l.union( [ t.classpart_slot[cp] for cp in t.parts_of(subj) ] )
    if len(aaa) >= 2 and None in aaa : print subj, ' '.join(map(str,aaa))

def show_unfilled():
    for subj in t.subjects :
        aaa = l.union( [ t.classpart_slot[cp] for cp in t.parts_of(subj) ] )
        if None not in aaa and len(t.remaining_names_of(subj))>0 :  print subj

ss = utf_util.read_from_clipboard(); print ss 

def cl() : 
    output = utf_util.read_from_clipboard() 
    print output
    return output

def export_time_slots(t_name) : 
    output = [ (cp, t.classpart_slot[cp]) for cp in t.classparts_of(t_name)]
    x.write_tuples_into_xlsx("ttt01.xlsx", output)


soph_subjects = [subj for subj in t.subjects if "1" in [ c[0] for c in t.members(subj) ] ]




