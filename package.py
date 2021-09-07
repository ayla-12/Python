# import travel.thailand # 임포트는 모듈이나 패키지만 가능. 바로 클래스를 붙이면 작동 X
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

from travel.thailand import ThailandPackage 
# travel 패키지 안, thailand 파일에서 ThailandPackage 패키지를 불러오세요
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam # travel 패키지 안, vietnam 파일을 불러오세요
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()


# travel 안에 있는 모든걸 쓰겠다는 건데 오류가 남
# 개발자가 문법 상에서 공개 범위를 설정을 해줘야하기 때문임
# __init__ 파일 안에 __all__을 통해서 공개 범위를 설정해 줄 수 있음!
