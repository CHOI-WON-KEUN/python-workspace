''' ImageCrawler
  기능 : 검색 키워드로 이미지를 검색하여 다운로드 받는다.
  저장할 이미지들은 현재 실행 파일의 하위 img 폴더 하단에 해당 키워드 폴더를 생성한 후 저장한다.
  kakao API를 사용하므로, 개발자 사이트(developers.kakao.com)에 가입한 후, 개발 앱을 생성하면 생성된 앱의 REST API Key를 이용한다.
  Image 검색 가이드 : developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-image
'''
import requests
import os

class ImageCrawler:
  '''ImageCrawler 클래스 :  검색 키워드로 이미지를 검색하여 다운로드 받는다.'''
  URL = 'https://dapi.kakao.com/v2/search/image' # 카카오 image 검색 API url
  __HEADERS = {'Authorization' : 'KakaoAK 7a22bc25aa04f9b5103211023bf8eb68'} # REST API 키(반드시 자신의 개인 키로 변경 필요!!)
  
  def __make_directory(self, keyword):
    '''검색 키워드(self.keyword)로 다운받을 이미지가 저장될 폴더를 생성한다.'''
    cwd = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 파일이 위치한 절대경로
    img_dir = os.path.join(cwd, 'img/' + keyword) # image 폴더 경로.
    
    if not os.path.exists(img_dir): # 저장할 폴더가 존재하지 않는 경우
      os.makedirs(img_dir) # 현재 파일 하위에 img/{keyword} 경로로 생성한다.
      
    return img_dir
  
  def __save_image(self, image_url, file_name):
    '''image_url을 통해 개별 이미지를 다운로드 받아서 file_name 파일명으로 저장하는 함수'''
    img_response = requests.get(image_url) # image_url 경로로 image를 요청
    print(file_name)
    
    if img_response.status_code == 200: # 요청에 성공했다면,
      with open(file_name, 'wb') as fp: # 이미지 파일 저장
        fp.write(img_response.content)
        
  def request_and_save_images(self, keyword):
    '''이미지를 검색하고, 검색 목록의 이미지를 모두 저장한다.
      검색 키워드(keyword) 파라미터를 받아서 검색 요청 data를 파라미터로 http 요청으로 검색 결과 목록을 받아온 후, 개별 이미지를 반복적으로 다운받아 저장한다.'''
    for p in range(2): # 페이지 수만큼 반복
      data = {'query' : keyword, 'page' : p + 1} # 검색 요청 data(기본 옵셥: 'page' : 1, 'size' : 80)
      img_dir = self.__make_directory(keyword) # 이미지 저장 경로 생성
      
      response = requests.post(ImageCrawler.URL, headers=ImageCrawler.__HEADERS, data=data) # 검색 요청
      
      if response.status_code != 200: # 요청에 실패했다면,
        print('error! because ', response.status_code) # error 코드 출력
      else: # 성공했다면,
        # print(response.json()) # 응답 문서 확인용 출력문
        count = p * 80 # 이미지 일련번호
        for image_info in response.json()['documents']: # json 형식의 응답 문서에서 documents를 반복 순회.
          count += 1 # image 번호
          # print(f'[{count}th] image_url = {image_info["image_url"]}') # 이미지 경로 확인용 출력문
          
          file_name = os.path.join(img_dir, f'{keyword}_{count}.jpg') # 저장될 이미지 파일명 저장
          self.__save_image(image_info['image_url'], file_name) # 이미지 저장

if __name__ == '__main__':
  img_crawler = ImageCrawler()
  img_crawler.request_and_save_images('나은이')
  img_crawler.request_and_save_images('아이유')