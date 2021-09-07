# 모듈
# 필요한 것들을 모아서 모듈화를 시키면 좋음

# import theater_module # 모듈 파일을 불러서 쓰겠다는 뜻
# theater_module.price(3) # 3명에서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명에서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv # as를 통해서 모듈의 풀네임을 쓰지 않아도 별명으로 사용가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # 모듈에 있는 함수를 그냥 사용하겠다는 뜻! 굳이 파일 출처를 적어주지 않아도 됨
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 어떤 함수만 쓸지 정할 수 있음
# price(5)
# price_morning(6)
# price_soldier(7) # 얘는 작동이 안됨! 모르기 때문

from theater_module import price_soldier as price # from import로 불러와도 as를 붙여 별명을 설정할 수 있음
price(2)
