
import random

stop = 0

while stop != 1:
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    print(dado_1, dado_2)
    stop = int(input('PARAR o dado colocar o valor 1 !'))
