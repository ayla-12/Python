# pip install
# 잘 만들어진 패키지 다운받아서 쓰기!

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pypi 라는 사이트에 많은 패키지가 있다

# 터미널에 입력하기
# pip list / 리스트 출력
# pip show 패키지이름 / 패키지 관련 정보
# pip uninstall 패키지이름 / 지우기
