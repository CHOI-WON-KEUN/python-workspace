# -*- coding: utf-8 -*-

import xlrd 
import re
import importlib
import list_util, xlsx_util, utf_util

import time_table as t 


#full_score_dict = dict( list_util.partition( 
#re.split(r'\s+', 
#'''국어I 20
#독서I 0
#독서III 0
#현대문학 20
#작문 0
#매체언어비평 20
#정치경제 50
#세계문화지리 30
#한국사 50
#세계사 60
#철학 50
#영어I 50
#영어회화I 0
#영어III 30
#고급커뮤니케이션 0
#영어독해 60
#영작문 10
#중국어I 50
#건강과체육I 0
#여가와체육I 0
#생활체육 0
#음악I 0
#생활음악 0
#미술I 0
#생활미술 0
#과학사 100
#융합과학탐구 0
#수리정보탐구 0
#수학I 60
#수학III 60
#기초통계학 60
#정수론 60
#미적분학I 70
#미적분학II 70
#선형대수학 70
#물리학I 100
#물리학III 100
#물리학실험I 0
#고급물리학I 30
#고급물리학II 30
#화학I 60
#화학III 60
#화학실험I 0
#고급화학I 30
#고급화학II 60
#생명과학I 40
#생명과학III 60
#생명과학실험I 0
#고급생명과학II 60
#지구과학I 60
#지구과학III 60
#컴퓨터과학I 50
#객체지향프로그래밍 50
#자료구조 50'''), 2))



full_score_dict = dict( list_util.partition( 
re.split(r'\s+', 
'''국어I	20 
수학I	60 
영어I	50 
정치경제	50 
컴퓨터과학I	50 
화학I	60 
생명과학I	40 
세계문화지리	30 
물리학I	100 
과학사	100 
수학III	60 
영어독해	60 
자료구조	50 
현대문학	20 
중국어I	50 
지구과학I	60 
철학	50 
정수론	60 
한국사	50 
영작문	10 
미적분학I	70 
객체지향프로그래밍	50 
고급물리학I	30 
고급물리학II	30 
영어III	30 
기초통계학	60 
물리학III	100 
화학III	60 
생명과학III	60 
고급화학I	30 
고급화학II	60 
고급생명과학II	60 
세계사	60 
미적분학II	70 
매체언어비평	20 
선형대수학	70 
지구과학III	60 
고급커뮤니케이션	40 
독서III	20 
독서I	20 
생명과학실험I	30 
수리정보탐구	40 
영어회화I	20 
융합과학탐구	40 
작문	20 
화학실험	20 
미술I	30'''), 2))

full_score_dict = dict( list_util.partition( 
re.split(r'\s+', 
'''객체지향프로그래밍 100
건강과체육I 100
고급물리학I 100
고급물리학II 100
고급생명과학II 100
고급커뮤니케이션 100
고급화학I 100
고급화학II 100
과학사 100
국어I 100
기초통계학 100
독서I 100
독서III 100
매체언어비평 100
물리학I 100
물리학III 100
물리학실험I 100
미술I 100
미적분학I 100
미적분학II 100
보건/진로 100
생명과학I 100
생명과학III 100
생명과학실험I 100
생활미술 100
생활음악 100
생활체육 100
선형대수학 100
세계문화지리 100
세계사 100
수리정보탐구 100
수학I 100
수학III 100
여가와체육I 100
영어I 100
영어III 100
영어독해 100
영어회화I 100
영작문 100
융합과학탐구 100
음악I 100
자료구조 100
작문 100
정수론 100
정치경제 100
중국어I 100
지구과학I 100
지구과학III 100
철학 100
컴퓨터과학I 100
한국사 100
현대문학 100
화학I 100
화학III 100
고급지구과학 100
창의융합특강XII 100 
창의융합특강XI 100 
창의융합특강I 100 
창의융합특강II 100 
창의융합특강V 100 
창의융합특강VIII 100 
창의융합특강VI 100 
창의융합특강IV 100 
창의융합특강X 100 
화학실험I 100'''), 2))



full_score_dict.update( dict( list_util.partition( 
re.split(r'\s+', 
'''총점 1000
객체지향프로그래밍 100
건강과체육II 100
고급물리학I 100
고급물리학II 100
고급생명과학I 100
고급화학II 100
고전문학 100
과학사 100
국어II 100
독서II 100
독서IV 100
매체언어비평 100
문법 100
물리학II 100
물리학IV 100
물리학실험II 100
미술II 100
미적분학I 100
미적분학II 100
보건/진로 100
생명과학II 100
생명과학IV 100
생명과학실험II 100
생활체육 100
선형대수학 100
세계문화지리 100
세계사 100
수리정보탐구 100
수학II 100
수학IV 100
시사영어 100
여가와체육II 100
영미문화탐구 100
영어II 100
영어소설 100
영어독해 100
영어회화II 100
예술사 100
융합과학 100
음악II 100
정수론 100
정치경제 100
정치와법 100
중국어II 100
지구과학II 100
지구과학III 100
철학 100
커뮤니케이션 100
컴퓨터과학II 100
한국사 100
현대문학 100
화학II 100
화학IV 100
화학실험II 100'''), 2)))



#def strip_typeinfo(c) :
    #if type(c) in [float, int ] :
        #return str(c)
    #elif type(c) is str :
        #return c
    #elif type(c) is unicode :
        #return re.sub(r'^[^\:]+:', '',  c).replace(u'\ufeff',
            #'').encode('utf-8')
    #else :
        #return ''


def read_scores(xls_name) : 
    output = [ ] 
    sheet = xlrd.open_workbook(xls_name).sheet_by_index(0)
    for i in range(sheet.nrows) : 
        output.append( list(map(xlsx_util.strip_typeinfo, sheet.row_values(i))) )
    return output

#def convert_romans( mystr ) :
    #conv_pairs = [("\xe2\x85\xa0", "I"), ("\xe2\x85\xa1", "II"),
            #("\xe2\x85\xa2", "III"), ("\xe2\x85\xa3", "IV"), (" ", "")]
    #output = mystr
    #for c in conv_pairs :
        #output = output.replace( c[0], c[1])
    #return output



#def get_index_subject_dict(rows) :  
#   index_subject = { }
#   for row in rows : 
#       if not (row[1] == "반" and row[3] == "번호" ) : 
#           continue 
#       for i, item in enumerate(row) : 
#           if re.search( r'\(\d\)|총점', item) : 
#               subj = convert_romans(re.sub( r'\(\d\)', '', item))
#               index_subject[i] = subj
#       return index_subject
#   else : 
#       return {}



def get_index_subject_dict_from_row(row) :  
    index_subject = { }
    if not (row[1] == "반" and row[3] == "번호" ) : 
        return {}
    else : 
        for i, item in enumerate(row) : 
            if re.search( r'\(\d\)|총점', item) : 
                subj = utf_util.convert_romans(re.sub( r'\(\d\)', '', item))
                index_subject[i] = subj
        return index_subject

def get_grade_num(rows) : 
    if rows[2][2].find("일람표") < 0 : 
        print( "Wrong data" )
        return None
    else : 
        r = re.search( r'\((\d)학년', rows[2][2])
        return r.group(1)

def read_name_from_row(row, grade_num_str) : 
    if not (row[1] == "반" and row[3] == "번호" ) : 
        if len(row[4]) > 0 : 
            if row[1].find("-") >= 0 : 
                return str( int( row[1].replace("-","")) * 100 + 
                            int(float(row[3])))  + row[4]
            else : 
                return str(int(grade_num_str)*1000  + 
                            100 * int(float(row[1])) 
                            + int(float(row[3]))) + row[4]
        else : 
            return ''
    else : 
        return ''


scores_data = {}

def read_scores_from_row(row, st_name, ind_subj_dict, full_sc_dict ) : 
    output = {}
    for i in ind_subj_dict : 
        if len(row[i]) > 0 : 
            output[ (st_name,  ind_subj_dict[i]) ] = \
                float(row[i]) * float(full_sc_dict[ ind_subj_dict[i] ]) / 100.0
    return output

def read_xls_scores(xls_names) : 
    scores_data = { }
    for f_name in xls_names : 
        print( "<{}>".format(  f_name))
        xl_rows = read_scores(f_name) 
        gr_str = get_grade_num(xl_rows)
        print( "{}학년".format( gr_str ) )

        curr_ind_subj = { } 
        curr_name = ''
        for row in xl_rows : 
            tmp_dict = get_index_subject_dict_from_row(row)
            if len(tmp_dict) > 0 : 
                curr_ind_subj = tmp_dict
                for k in curr_ind_subj : 
                    print( k, curr_ind_subj[k], end = " " )
                print()   
            tmp_name = read_name_from_row(row, gr_str)
            if len(tmp_name)>0 : 
                print( tmp_name )
                tmp_scores = read_scores_from_row(row, tmp_name, curr_ind_subj, 
                                    full_score_dict)
                scores_data.update(tmp_scores)
    return scores_data



def get_name_class_scores( name_subj_scores ) : 
    name_class_scores = { } 
    for neis_st_name, subj in name_subj_scores : 
        if neis_st_name in t.names : 
            st_name = neis_st_name 
        else : 
            st_name = t.name(neis_st_name)
            if st_name is None : 
                continue
        cl = t.para_classname(t.name_subject_class(st_name, subj))
        name_class_scores[ (st_name, cl) ] = name_subj_scores[ 
                                                    (neis_st_name, subj)]
    return name_class_scores 



if __name__ == "__main__" : 
    import sys 
    xls_names = sys.argv[1:]
    for f_name in xls_names : 
        print( "<{}>".format(  f_name ))
        xl_rows = read_scores(f_name) 
        gr_str = get_grade_num(xl_rows)
        print( "{}학년".format(  gr_str))

        curr_ind_subj = { } 
        curr_name = ''
        for row in xl_rows : 
            tmp_dict = get_index_subject_dict_from_row(row)
            if len(tmp_dict) > 0 : 
                curr_ind_subj = tmp_dict
                for k in curr_ind_subj : 
                    print( k, curr_ind_subj[k], end=" ")
                print()   
            tmp_name = read_name_from_row(row, gr_str)
            if len(tmp_name)>0 : 
                print( tmp_name )
                tmp_scores = read_scores_from_row(row, tmp_name, curr_ind_subj, 
                                    full_score_dict)
                scores_data.update(tmp_scores)

    print( "Saving <ttt02.xlsx>")
    xlsx_util.write_dict_into_xlsx("ttt02.xlsx", scores_data)

    t.load()
    importlib.reload(t)
    ncs_data = get_name_class_scores( scores_data ) 
    print( "Saving <ttt03.xlsx>" )
    xlsx_util.write_dict_into_xlsx("ttt03.xlsx", ncs_data)
    



