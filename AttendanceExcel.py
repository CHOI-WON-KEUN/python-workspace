''' 출석부출력(담임용) 파일 리스트를 읽어 출결 명부를 작성.
'''
import os
import pandas as pd
import xlrd
import AttendanceCheck as ac

# for f in file_list:
#   file_path = os.path.join(xl_dir, f)
#   excel = xl.load_workbook(os.path.join(xl_dir, f))
#   df = pd.read_excel(os.path.join(xl_dir, f))
#   print(df.head())
#   print(file_path)

cwd = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 파일이 위치한 절대경로
xl_dir = os.path.join(cwd, 'excel') # excel 폴더 경로.

file_list = os.listdir(xl_dir)
file_path = os.path.join(xl_dir, file_list[0])
print(file_path)

a = ac.AttendanceCheck(file_path)