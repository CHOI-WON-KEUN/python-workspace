# -*- coding: utf-8 -*-


import sys

import semester as sem
import sugang as sg

import xlsx_util, list_util

def read_name_subjects(fname):
    data = list_util.transposed( 
        xlsx_util.read_xlsx_sheet_into_list(fname, sheet_name="Sheet2"))
    output = [ ]
    for row in data :
        subj = row[0]
        if len(subj)>0:
            for st_name in row[1:] :
                if len(st_name) > 0 :
                    list_util.check_append(output, (st_name, subj),
                        lambda x: ' '.join(x) , silent=True)
    return sg.change_subject_names(output, change_dict = { } )


source_fname = sg.stats_dir + "/수강신청현황-" + sys.argv[1] + ".xlsx"

target_fname = sg.stats_dir + "/수강신청현황-" + sys.argv[2] + ".xlsx"

pairs_one = read_name_subjects(source_fname)
pairs_two = read_name_subjects(target_fname)


print "%d pairs has been read from %s" % (len(pairs_one), source_fname) 
print "%d pairs has been read from %s" % (len(pairs_two), target_fname) 

p_diffs = sg.pair_differences(pairs_one, pairs_two)

output_fname = sys.argv[1] + "-" + sys.argv[2] + ".xlsx"

sg.export_differences_into_xlsx(output_fname, p_diffs)




