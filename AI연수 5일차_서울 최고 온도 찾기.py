import csv
f = open("C:\\Users\\SSHS\\Desktop\\업무\\연수\\2021 AI 관련 교과 융합 연수(비대면 실시간)\\seoul.csv", "r", encoding="cp949")
data = csv.reader(f, delimiter = ",")
header = next(data)
max_temp = -999
max_date = ""

for row in data:
    if row[-1] == "":
        row[-1] = -999
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_date = row[0]
        max_temp = row[-1]
print(f"최고기온 : {max_temp}, 그 때의 날짜는 {max_date} 입니다.")
f.close()