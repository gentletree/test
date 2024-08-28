def chephone():
    phoneNumber=input('输入你的手机号码：')
    numlenth=len(phoneNumber)
    CN_mobile= [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158,
                159,182,183,184,187,188,147,178,1705]
    CN_union=[130,131,132,155,156,185,186,145,176,1709]
    CN_telecom =[133,153,180,181,189,177,1700]
    first_three=int(phoneNumber[0:3])
    first_four=int(phoneNumber[0:4])
    if numlenth!=11:    #感叹号在这里表示，逻辑运算中表示“非”。 not True 会返回False。
        print('不是11位数啊!输错了啊!!!')
        chephone()
    elif first_three in CN_mobile or first_four in CN_mobile:
        print('运营商：中国移动')
        print('等下给你发验证码',phoneNumber)
    elif first_three in CN_union or first_four in CN_union:
        print('运营商：中国联通')
        print('等下给你发验证码',phoneNumber) 
    elif first_three in CN_telecom or first_four in CN_telecom:
        print('运营商：中国电信')
        print('等下给你发验证码',phoneNumber)
    
    else:
        print('都不是电话号码！')
        chephone()
chephone()