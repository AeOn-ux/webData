import requests

# requests url 정보를 가져옴
# url = "http://www.naver.com"
url = "http://www.google.com"
res = requests.get(url)
# status_code : 실행코드 출력
# raise_for_status:에러시 종료
res.raise_for_status() # 에러시 프로그램 종료
print("응답코드 :",res.status_code) 
# 1XX: Informational(정보 제공), 2XX: Success(성공), 3XX: Redirection(리다이렉션), 4XX: Client Error(클라이언트 에러), 5XX: Server Error(서버 에러)
print(requests.codes.ok) # 성공코드 출력 : 200

print(res.text)