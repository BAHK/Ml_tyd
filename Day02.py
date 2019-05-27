import math


"""
使用变量保存数据并进行算术运算

Version: 0.1
Author: 骆昊
"""

a = 321
b = 123

print( a + b )
print( a - b )
print( a * b )
print( a / b )
print( a // b )
print( a % b )
print( a ** b )


"""
使用input函数输入
使用int()进行类型转换
用占位符格式化输出的字符串

Version: 0.1
Author: 骆昊
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))




"""
运算符的使用

Version: 0.1
Author: 骆昊
"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)







"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
"""

f = float(input("请输入华氏温度:"))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f,c)) 





"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""

radius = float(input('圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % perimeter)


"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""

year = int(input('请输入年份: '))
is_leap = (year % 4 == 0 and year % 100 != 0 or
        year % 400 == 0)

print(is_leap)




