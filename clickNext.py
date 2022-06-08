''' pyautogui를 활용한 매크로 기능 구현
설명: 메인 화면에 특정 이미지가 노출되면 마우스 포인터를 이동하여 클릭한다. 매 5초마다 작동한다.

1. saveImage() 함수를 먼저 활성화하여 화면 중에서 클릭할 이미지 영역을 지정하여 저장한다.
저장된 이미지는 현재 파일 경로 하위에 'media/img/capture_img.jpg'로 저장된다.
저장된 이미지의 이름을 필요에 따라 'Next.jpg' 또는 'Play.jpg'로 이름을 변경한다. (현재 버전은 2개까지 지원됨. 필요에 따라 추가 가능.)

2. runAll() 함수를 실행하면 저장한 이미지가 메인화면(듀얼 모니터인 경우에 주화면)에 노출될 때, 마우스 포인터가 이동하여 클릭을 시도한다.
매 5초마다 시도하며 터미널에 시도 횟수와 이미지 찾기 성공 여부가 표시된다.
'''
import os
import pyautogui as pag # pip install pyautogui
# import matplotlib.image as img 
# import matplotlib.pyplot as plt
import keyboard # pip install keyboard
import time

# 클릭 시도 횟수 카운터 변수
cnt = 0 # 클릭 회수 저장할 전역변수 초기화

# 이미지 불러오기
cwd = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 파일(clickNext.py)의 경로
img_dir = os.path.join(cwd, 'media\\img') # 이미지가 존재하는 폴더 경로. C:\Users\SSHS\Desktop\WorkSpace\PythonWorkSpace\Pangjae\media\img

# 불러온 이미지 확인용 - 삭제 가능
# ndarray = img.imread(next_btn_path) # 이미지 불러오기
# plt.imshow(ndarray) # 이미지 출력 준비
# plt.show() # 이미지 출력

# 저장할 이미지 영역을 구한다.
def getCaptureRegion():
  '''이미지 영역 구하기: 
     저장할 이미지의 좌상단과 우하단에 마우스를 위치하고 F4를 각각 누르면,
     해당 영역의 좌표 좌상단 x, y 좌표와 가로, 세로의 크기를 tuple 형식으로 반환한다.'''
  p1, p2 = None, None
  print('저장할 이미지 영역의 좌상단에 마우스를 위치한 후 "F4"를 누르세요.')
  while True:
    if keyboard.is_pressed('F4'):
      p1 = pag.position()
      print(p1)
      time.sleep(0.5)
      break
  print('저장할 이미지 영역의 우하단에 마우스를 위치한 후 "F4"를 누르세요.')
  while True:
    if keyboard.is_pressed('F4'):
      p2 = pag.position()
      print(p2)
      time.sleep(0.5)
      break
  return (p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1]) # 영역 반환 (x, y, w, h)

# 지정된 영역의 이미지를 저장한다.
def saveImage():
  '''이미지 저장:
     화면상의 특정 이미지의 사각형 영역을 구해서, 현재 파일이 폴더 하단의 이미지 폴더에 jpg 포맷으로 저장한다.'''
  # global img_dir
  cap_region = getCaptureRegion() # 영역 지정
  print(cap_region)
  path = os.path.join(img_dir, 'capture_img.jpg') # 이미지 저장 경로
  pag.screenshot(path, region=cap_region) # 화면 캡쳐 저장

# 찾는 이미지가 노출되면 마우스 포인터를 이동시킨 후 클릭을 시도한다.
def searchAndClick(img, conf):
  '''검색 및 클릭:
     전체 화면 중에서 지정된 이미지가 노출되면 마우스 포인터를 이동한 후 클릭한다.'''
  global cnt # 클릭 회수 저장할 전역변수
  
  # 모니터 화면 중에서 해당 이미지 영역 찾기
  p_list = list(pag.locateAllOnScreen(img, confidence=conf)) # 타겟 이미지 검색. 다수 개 가능
  print("타겟 찾음" if p_list else "못찾음") # 검색 성공 여부 출력
  
  if p_list:
    p_pos = pag.position() # 현재 마우스 포인터 위치 저장.
    next_loc = p_list[0] # 여러 개 발생시 첫번 째를 기준으로
    # 버튼 클릭 시도
    pag.click(next_loc.left + next_loc.width // 2, next_loc.top + next_loc.height // 2) # mouse 포인터 위치 이동 후 클릭
    cnt += 1 # 클릭 시도 횟수 증가
    print(cnt)
    pag.moveTo(p_pos) # 마우스 포인터 위치를 원래 위치로 이동

# 매 5초마다 무한 반복으로 찾는 이미지가 노출된 경우 해당 이미지 위에서 마우스 클릭을 한다.
def runAll():
  next_btn_path = os.path.join(img_dir, 'Next.jpg') # Next 버튼 경로
  play_btn_path = os.path.join(img_dir, 'Play.jpg') # Play 버튼 경로
  youtube = os.path.join(img_dir, 'youtube.jpg') # youtube 버튼 경로
  
  while True:
    # searchAndClick(next_btn_path, 0.85) # 정밀도 수치를 조절할 필요가 있음.
    # searchAndClick(play_btn_path, 0.75) # 정밀도 수치를 조절할 필요가 있음.
    searchAndClick(youtube, 0.75) # 정밀도 수치를 조절할 필요가 있음.
    time.sleep(5) # 5초간 대기

if __name__ == '__main__':
  # 다음 명령어 2가지 중에서 1가지씩만 사용해야 함!! 
  # 1단계: saveImage() 활성화하여 이미지를 저장한다.
  # 2단계: runAll() 활성화하여 매크로를 실행한다. 필요시 저장된 타겟 이미지를 추가한다. 종료시 콘솔창에서 Ctrl+C
  
  # saveImage() # 이미지 영역 저장시에만 사용. 매크로 작동시 주석 처리함.
  runAll() # 실제 매크로 작동시에만 사용. 이미지 영역 저장시에는 주석 처리함.
