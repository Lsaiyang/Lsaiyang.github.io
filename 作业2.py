#        是否是会员，给予优惠1
#if is_plus:######
    #print('欢迎地主家的傻儿子')
    #n = int(input('您买的东西金额为:'))
    #print('由于您是会员，给您打八折{0:2f}'.format(n*0.8))

#print('欢迎光临')
#n = int(input('您买的东西金额为:'))

#print('谢谢光临')
#=========================================
#         是否是会员，给予优惠2
#is_plus = True#是否是会员
#price = input('price')
#price = int(price)
#if is_plus:#####
    #price = price * 0.8
#else:
    #price = price * 0.95

#print('价格是{}'.format(price))

#========================================
#          超时打折1
#n = input('请输入你的购买金额：')
#n= int(n)
#if n < 0:
#    print('非法金额')
#else:
#    if n > 400:
#        n= n * 0.85
#    else:
#       n= n * 0.95
#    print('实际购买金额为 %.2f' % n)

#====================================
#             超市打折2
#n = input('请输入你的购买金额：')
#n = int(n)
#if

#=========================================
#       测身高
#n = input('请输入身高：')
#n =float(n)
#if n > 1.2:
#    print('成人票')
#else：
#    print('儿童票')

#===========================================
#       分数判断
#   break  用法
# while True:
#    n = int(input('分数：'))
#    if n > 100 or n < 0:
#        print('无法判断')
#        break
#    elif 90 <= n:
#        print('A')
#    elif 80 <= n:
#        print('B')
#    elif 70 <= n:
#        print('C')
#    elif 60 <= n:
#        print('D')
#    elif n < 60:
#        print('F')

#=====================================
#      输入五次成绩，算总成绩，平均值
# lsy = 1
# dd = 0        #随便取啥，不要是关键字
# while True:
#     n = int(input('请输入第{}科成绩:'.format(lsy)))
#     if n > 100 or n < 0:
#         print('请重新输入')
#         continue
#     dd = dd + n
#     if lsy >= 5:
#         print("总成绩为:{},平均成绩为:{}".format(dd,dd/lsy))
#         break
#     lsy += 1

#=========================================
#        9,9乘法表    1
# i = 1
# while i <= 9:
#     j = 1
#     x =''
#     while j <= i:
#         x += ('{0:d} x {1:d} = {2:2d} |'.format(j,i,i*j))
#         j += 1
#     print(x)
#     i+= 1

#       9，9乘法表    2
# i = 1
# while i <= 9:
#     j = 9
#     x = ""
#     while j >= i:
#         x +="{0:d} x {1:d} = {2:2d}|".format(i,j,i*j)
#         j -= 1
#     print(x)
#     i +=1

#===========================================
#             打印梯子型数字
# i = 1
# n = 9
# space_num = n -1
# while space_num >= 0:
#     string = (' '*space_num)
#     j = 0
#     while n - space_num > j:
#         string += str(i%10) + " "
#         i += 1
#         j += 1
#     print(string)
#     space_num -= 1

#==============================
#         打印正三角形*1
# i = 1
# while i < 6:
#     print("*"*i)
#     i += 1

 #        打印三角形*2
# i = 6
# while i > 0:
#     print('*'*i)
#     i -= 1

#===================================
#              函数
# def mingzi(n,y,x):
#     print(y,x)
#     if n % 2 == 0:
#         raise  Exception('必须是技术')
#     mid = n // 2 + 1  # 中间一排
#     i = 1
#     while n > 0:
#         space_num = abs(mid - i)
#         base_num = mid - space_num
#         star_num = base_num * 2 - 1
#         if base_num !=1:
#             print(' ' * space_num + '*' +' '* (star_num-2)+'*')
#         else:
#             print(' '*space_num +'*')
#         i += 1
#         n -= 1
# mingzi(13,'asdf','asd')
# mingzi(23,'hhhh','ddddd')
# mingzi(17,'!!!!','$$$$$')
# mingzi(27,'DAD','dawd')

#=================================
#        返回值1
# amount = 50
# def discount(t):#     amount随便去什么
#     global amount
#     amount = amount * 0.8
#     return amount
# x = discount(20)
# print(x)
# type(x)
#
# #        返回值2
# def discount(amount):#     amount随便去什么
#     amount = amount * 0.8
#     return amount
# x = discount(20)
# print(x)

#====================================
#             递归函数1
# def sui(n):
#     if n > 16:
#         return n
#     return sui(2*n)
# x = sui(2)
# print(x)
#1. sui(2)       输入数字2，乘了2，等于4
#    return 32
#      --->sui(4)       等于（4）又回到开始，又乘以2，得8
#          return 32
#            --->sui(8)        得（8）又乘以2，得16
#                return 32
#                --->sui (16)       得（16）又乘以2，得32
#                     return 32
#                     --->sui (32)    『因，得（数字）乘以2，（而数字）是16，所以，得（数字）不能超过16，最后的答案不能超过16乘以2
#                          return 32

#=============================================
#         递归函数2
# def plus(n):
#     if n == 1:
#         return  n
#     else:
#         return  n + plus(n - 1)
# print(plus(5))

