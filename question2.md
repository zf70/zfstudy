import random
number = random.randint(1,100)
print('猜数！您只有5次机会！')
n = 0
while n < 5:
    n = n + 1
    guess = int(input("猜猜看："))
    if number == guess:
        print('猜中了!')
        break
    elif number < int(guess):
        print('大了，再来一次！')
    else:
        print('小了，再来一次！')
print('游戏结束！数字是：',number)
