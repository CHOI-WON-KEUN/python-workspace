import os
import pandas as pd

# 학생이 제출한 수강신청계획서 파일명을 리스트로 만들어서 메모장에 옮기기
file_path = "C:\\Users\\SSHS\\Desktop\\Python Workspace\\plan-files"
file_names = os.listdir(file_path)
with open("file_names.txt", "w", encoding="utf-8") as f:
    for name in file_names:
        f.write(name+"\n")

df = pd.read_excel("C:\\Users\\SSHS\\Desktop\\Python Workspace\\이름수정작업용.xlsx", usecols=[7, 9])
# print(df)
old_name = pd.read_excel("C:\\Users\\SSHS\\Desktop\\Python Workspace\\이름수정작업용.xlsx", usecols=[7])
new_name = pd.read_excel("C:\\Users\\SSHS\\Desktop\\Python Workspace\\이름수정작업용.xlsx", usecols=[9])
