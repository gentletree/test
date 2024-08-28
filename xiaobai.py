# word = 'a loooooong word'#16 len
# num = 12
# string = 'bang!'
# total = string * (len(word) - num) #􁒵􀕰􀔭􀨁􁒧􀔀'bang!'*4
# print(total)

# phone_number = '1386-666-0006'
# hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
# print(hiding_number)

# print('{} a word she can get what she {} for.'.format('With','came'))
# print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
# print('{0} a word she can get what she {1} for.'.format('With','came'))

# city = input("write down the name of city:")
# url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

# def fahrenheit_converter(C):
#  fahrenheit = C * 9/5 + 32
#  return str(fahrenheit) + '°F'

# C2F = fahrenheit_converter(88)
# print(C2F)

# def weight_converter (W):
#     weight = W/1000
#     return str(weight)+"kg"
# kk=weight_converter(1000)
# print(kk)

# import math
# def zhijiaobian(a,b):
#     xiebian=math.sqrt(a**2+b**2)
#     return str(xiebian)

# long=zhijiaobian(5,4)
# print('the third side is'+long)



# def text_create(name, msg):
#    desktop_path = '/Users/Hou/Desktop/'
#    full_path = desktop_path + name + '.txt'
#    file = open(full_path,'w')
#    file.write(msg)
#    file.close()
#    print('Done')
# def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
#     return word.replace(censored_word, changed_word)
# def censored_text_create(name, msg):
#     clean_msg = text_filter(msg)
#     text_create(name,clean_msg)
# censored_text_create('Try','lame!lame!lame!')

# 1 > 2 # False
# 1 < 2 <3


# def account_login():
#     password = input('Password:')
#     if password == '12345':
#         print('login success!')
#     else:
#         print('wrong password')
#         account_login #运行函数
# account_login()  #调用函数
    

# password_list=['ccccc','12345']

# def account_login():
#     password = input('Password:')
#     password_correct= password==password_list[-1]
#     password_reset= password==password_list[0]
#     if password_correct:
#         print('login success')
#     elif password_reset:
#         new_password = input('Enter a new password:')
#         password_list.append(new_password)
#         print('Your password has changed successfully')
#         account_login()
#     else:
#         print('Wrong password or invalid input!')
#         account_login()
# account_login()


# for num in range(1,11):
#     print (str(num)+' + 1 =',num+1)

# songslist=['AA','BB','CC']
# for song in songslist:
#     if song == 'AA':
#         print(song,'aaaaa')
#     elif song =='BB':
#         print(song,'bbbb')
#     elif song =='CC':
#         print(song,'cccc')

# for i in range(1,10):
#     for j in range(1,10):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print() #打完每一行后换行


# import random

# num=list(range(1,11))
# random.shuffle(num)
# print (num)


# count=0
# while True:
#     print('good xxxxxx')
#     count=count+1
#     if count==10:
#         break


# import os

# desktop_path=os.path.join(os.path.expanduser('~/Desktop'),'textfiles')
# if not os.path.exists(desktop_path):
#     os.makedirs(desktop_path)

# for i in range(1,11):
#     file_name=f'{i}.txt'
#     file_path=os.path.join(desktop_path,file_name)
#     with open(file_path,'w') as file:
#         file.write('good。\n')
# print('储存在'+ desktop_path,'done')


# def invest(amount, rate, time):
#     print('本金：{}'.format(amount))
#     for t in range(1, time+1):
#         amount=amount*(1+rate)
#         print('第{}年：￥{}'.format(t,amount))

# if __name__ =='__main__':  #_name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
#                            #这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
#     amount=float(input('请输入金额：'))
#     rate=float(input('请输入年利率：'))
#     time=int(input('请输入投资时间：'))
#     invest(amount,rate,time)

# for i in range(0,101):
#     if i%2==0:
#         print(i)


# import random 
# def roll_shaizi(numbers=3, points=None):  #创建函数，设定两个默认参数作为可选，points：三个筛子点数的列表
#     print('<<<<<ROLLING IN THE DEEP>>>>>')
#     if points is None:  #如果参数中并未指定points，那么为points创建空的列表
#         points=[]
#     while numbers > 0:
#         point=random.randrange(1,7)
#         points.append(point)
#         numbers=numbers-1
#     return points

# def roll_result(total):
#     isBig =11 <=total <=18
#     isSmall = 3 <= total <=10
#     if isBig:
#         return'Big'
#     elif isSmall:
#         return'Small'

# def start_game():
#     print('<<<<<$$$$$ LET US GO !!!! $$$$$>>>>>')
#     choices=['Big','Small']
#     your_choice= input('Big or Small:')
#     if your_choice in choices:
#         points= roll_shaizi()
#         total= sum(points)
#         youWin=your_choice==roll_result(total)
#         if youWin:
#             print('The points are',points,'You win!!!')
#         else:
#             print('The points are',points,'You lose!!!!')
#     else:
#         print('Invalid Words')
#         start_game()
# start_game()


# import random

# global moneyAll #设置moneyAll为全局变量。
# moneyAll = 1000

# def roll_dice(numbers=3, points=None):
#     print('<<<<<  ROLL THE DICE!  >>>>>')
#     if points is None:
#         points=[]
#     while numbers>0:
#         point= random.randrange(1,7)
#         points.append(point)
#         numbers=numbers-1
#     return points

# def roll_result(total):
#     isBig=11<= total<=18
#     isSmall=3<=total<=10
#     if isBig:
#         return 'Big'
#     elif isSmall:
#         return 'Small'
    
# def start_game():
#     global moneyAll  #这里需要使用到上面设置的全局变量，所以需要重新声明
#     print('<<<<<$$$$$ LET US GO !!!! $$$$$>>>>>')
#     choices=['Big','Small']
#     your_choice=input('Big or Small:')
#     if your_choice in choices:
#         your_bet= int(input('你要氪金多少啊？'))
#         if moneyAll>=your_bet:
#             points=roll_dice()
#             total=sum(points)
#             youWin=your_choice==roll_result(total)
#             if youWin:
#                 print('点数是',points,'不错嘛！')
#                 moneyAll+=your_bet   #+= 是赋值运算符  c += a 等共同 c=c+a
#                 print('你赢了',your_bet,'你现在还有',moneyAll,'钱')
#                 start_game()
#             else:
#                 print('点数是',points,'小菜鸡！')
#                 moneyAll-=your_bet
#                 print('你输了',your_bet,'你现在还剩',moneyAll,'钱')
#                 if moneyAll==0:
#                     print('滚回家吧！')
#                 else:
#                     start_game()
#         else:
#             print('不够钱')
#             start_game()
#     else:
#         print('Invalid Words')
#         start_game()
# start_game()



















