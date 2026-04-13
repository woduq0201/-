import random

print("** 로또 추첨을 시작합니다. **")

numbers = random.sample(range(1,46),6)
numbers.sort()

print("추첨된 로또 번호 ==>", *numbers )