''' 출결 집계 파일 생성
    주차별 출결 파일에서 출결 현황을 DataFrame 형식으로 집계한다.'''
import os
from numpy.core.arrayprint import DatetimeFormat
import pandas as pd
from   datetime import datetime

class AttendanceCheck:
  '''출결 집계 : 주차별 엑셀 파일을 읽어 집계함.'''
  CLOSE_CONFIRM_CTG = {'인정'   : ['△', '◁',  '▷', '▽'] # 출석인정
                     , '질병'   : ['♡', '＃', '＠', '☆']
                     , '미인정' : ['♥',  'X',  '◎', '◇']
                     , '기타'   : ['▲',  '≠',  '∽', '=']} # 마감 결과 범례 카테고리
  CLOSE_CONFIRM_NM_LIST = ['결석', '지각', '조퇴', '결과'] # 마감 결과 범례 이름 리스트
  CLOSE_CONFIRM_DF = pd.DataFrame(CLOSE_CONFIRM_CTG, index=CLOSE_CONFIRM_NM_LIST) # 마감 결과 범례 DataFrame
  S_ROW = 5 # 데이터 테이블 시작 줄 번호

  def __init__(self, xlfile_path):
    '''출결 집계 초기화 함수 : 주단위 출결 엑셀 파일을 입력받아 집계표 형식으로 작성한다.'''
    print('파일명:', xlfile_path)
    
    self.xl_data = pd.read_excel(xlfile_path) # 출결 엑셀 파일을 읽어온다.
    self.aggregateDF = pd.DataFrame(columns=['날짜', '학번', '이름', '시간', '출결']) # 결과 출결 DF
    self.__aggrigateAttendance() # 출결 현황을 집계한다.
    
  def __aggrigateAttendance(self):
    '''출결 집계 함수 : 주차별 엑셀 파일을 읽어 마감에 표시가 있는 학생의 경우 집계표를 작성한다.'''
    df = self.xl_data[1:-2] # 첫 줄(분반, 출석부)과 마지막 두 줄(범례와 공백줄)을 제거함.
    # print(df)
    date_col     = [ 2, 14, 26, 38, 50] # 2번째 행의 날짜 정보가 기재된 컬럼들
    deadline_col = [13, 25, 37, 49, 61] # 마감 정보가 기재된 컬럼들
    
    classroom = df.iloc[0, 0] # 분반 (예) 3학년 과학과 7
    print(classroom)
    prefixID  = str(classroom[0]) + str(classroom[-1]) # 학번 앞자리 (예) 3학년 과학과 7 ==> 37
    dateList  = self.__transWeekdate2List(df.iloc[1, date_col]) # 주별 날짜 Series를 문자형 날짜 리스트로 변환 (예) 05월31일(월), 06월01일(화), ... ==> 20210531, 20210601, ...
    schoolIDs = self.__getSchoolIDList(df.iloc[AttendanceCheck.S_ROW:, 0], prefixID) # prefixID와 일련번호로 학번 리스트를 생성
    names     = self.__getNameList(df.iloc[AttendanceCheck.S_ROW:, 1]) # 학생 성명 리스트를 생성
    
    for col in deadline_col: # 출결 마감 컬럼별 순회
      dt = dateList[col // 12 - 1] # 날짜 표기된 컬럼 위치 리스트
      aggrigateCol = self.__aggrigateCol(df, col) # 출결 마감 컬럼별 기재된 내용을 리스트로 받아온다.
      for i, d in enumerate(aggrigateCol): 
        if d: # 출결 표기가 존재하는 경우
          idx = d.index(':')
          self.aggregateDF = self.aggregateDF.append({'날짜': dt, 
                                                      '학번': schoolIDs[i], 
                                                      '이름': names[i], 
                                                      '시간': d[:idx], 
                                                      '출결': d[idx + 1:]}, 
                                                      ignore_index=True) # 결과 데이터프레임에 추가한다.

  def __aggrigateCol(self, df, col):
    '''마감 컬럼의 마크를 확인해서 출결 마감 리스트를 작성하여 반환한다.'''
    resultList = []
    for i, mark in enumerate(df.iloc[AttendanceCheck.S_ROW:, col]): # 해당 마감 컬럼의 모든 데이터 행을 반복
      s = None
      for k, v in AttendanceCheck.CLOSE_CONFIRM_CTG.items(): # 마감 카테고리가 
        if mark in v: # 마감 마크가 포한된 항목을 찾는다.
          s = k + AttendanceCheck.CLOSE_CONFIRM_NM_LIST[v.index(mark)] # 출결 구분 (예) 인정결석, 인정지각, ......
          s += ':' + self.__getFrom2EndTime(list(df.iloc[i + AttendanceCheck.S_ROW, col-11:col])) # 출결 시간 추가 (예) :전일, :조회~2교시
          break # 출결 사유와 시간을 저장하였으면 내부 루프를 종료한다. 
      resultList.append(s) # 결과 리스트에 추가한다.
    return resultList
  
  def __getFrom2EndTime(df, mark_list):
    '''마감 마크가 있는 경우 해당 시간의 시작과 끝 교시에 대한 결과를 문자열로 반환한다.'''
    l = [i for i, v in enumerate(mark_list) if v == '/'] # 출결 표기('/')가 된 인덱스 리스트
    
    f, e = l[0], l[-1] # 시작과 끝 교시 기록
    if f == 0 and e >= 7: # 출결 표기가 조회부터 종례까지 모두 입력된 경우
      return '전일'
    else:
      s = ''
      s += '조회' if f == 0 else f'{f}교시' # 출결 시작 표기
      s += '-' # 연결선
      s += '종례' if e >= 7 else f'{e}교시' # 출결 종료 표기
      return s

  def __transWeekdate2List(self, dateSeries):
    '''주별 날짜 Series 데이터를 문자형 날짜 포맷 리스트로 변환하여 반환한다.'''
    yy = str(datetime.today().year) # 오늘 날짜의 년도 스트링
    return [yy + '-' + d[0:2] + '-' + d[3:5] for d in dateSeries] # 2021-05-31, 2021-06-01, ......
  
  def __getSchoolIDList(self, idSeries, prefixID):
    '''학번 Series와 학번 접두사로 4자리 학번 리스트를 생성하여 반환한다.'''
    return [prefixID + '%02d' % no for no in idSeries]
  
  def __getNameList(self, nameSeries):
    '''성명 Series로 성명 리스트를 생성하여 반환한다.'''
    return [nm for nm in nameSeries]
    
  def __str__(self):
    return str(self.aggregateDF)

if __name__ == '__main__':
  cwd = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 파일이 위치한 절대경로
  xl_dir = os.path.join(cwd, 'excel') # excel 폴더 경로.
  file_list = os.listdir(xl_dir) # excel 폴더내 모든 파일 목록.
  print(file_list)
  
  totalDF = pd.DataFrame() # 전체 통합 결과 DataFrame
  for f in file_list:
    totalDF = totalDF.append(AttendanceCheck(os.path.join(xl_dir, f)).aggregateDF, ignore_index=True, sort=False) # 파일별 집계 내용을 누적 추가한다.

# print(totalDF.sort_values(['날짜', '학번']))
aggregateXlFile = os.path.join(cwd, '출결집계.xlsx')
# df = pd.DataFrame(totalDF)
# writer = pd.ExcelWriter('출결집계.xlsx', 
#                         engine='xlsxwriter',
#                         date_format='yyyy-mm-dd')
# df.to_excel(writer, sheet_name='출결집계')
# writer.save()
totalDF.to_excel(aggregateXlFile, sheet_name='출결집계')