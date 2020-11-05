"""
#1、注释的用法：单行#，多行三个引号
#查看类型的函数type()
A = 10
b = "hi python"
c = 12.3
print(type(A))
print(type(b))
print(type(c))"""

# 2、关键词
# a, b = 2, 4
# while True:
#     if a > b:
#         print("a>b")
#     else:
#         print("a<b")
#         break

# 3、with...as 用法同 try...finally,如：执行顺序（open、赋值、read、close）
# file = open("/tmp/foo.txt")
# try:
#     data = file.read()
# finally:
#     file.close()
# # 等同
# with open("/tmp/foo.txt") as file:
#     data = file.read()

# 4、全局变量 global用法一
# NAME = "xueweihan"
#
#
# def set_name(name_value):
#     global NAME
#     NAME = name_value
#     print("输出全局变量NAME的值:", NAME)
#
#
# # 为全局变量重新赋值
# print("输出赋值完的全局变量NMAE的值:", NAME)
# set_name("123xueweihan")


# 4.1、全局变量 global用法二 __globals__打印全部全局变量
# def other():
#     print(en) # 此处结果为0，en = 0全局没生效，需要用global en
#
# def out():
#     # global关键字作用
#     global en
#     en = 2
#     # 调用other可以打印en，去掉global会报错。
#     other()
#     print(out.__globals__)
#
#
# out()

# 5.断言assert [表达式,参数]：
#  true 继续执行；
#  false 抛异常，并打印出断言后的值，如此列子执行结果为：AssertionError: n is zero!
#
# def foo(s):
#     n = int(s)
#     assert n != 2, 'n is zero!'
#     return 10 / n
#
# print(foo('2'))

# 6.pass不做任何事，用于占位； 如：输出 abc 的每个字母，执行结果为
# >>>当前字母 : a
# >>>这是 pass 块! b
# >>>当前字母 : c
# for letter in 'abc':
#     if letter == 'b':
#         pass
#         print('这是 pass 块!',letter)
#     else:
#         print('当前字母 :', letter)

# 7.yield的用法：类似return 且是个生成器
# def foo():
#     print("starting...")
#     while True: # 8.从two来时，未执行yield，所以进入循环
#         res = yield 4 # 3.从first来，第一次执行 return返回4，但未赋值给res；9.第二次执行 return返回4，未赋值给res;
#         print("res:",res)   # 7.从two来，第一次执行，因为之前res没赋值，打印res：none
# g = foo()   # 1.不会真的执行foo函数，遇到yield 得到生成器给g
# print("first", next(g)) # 2.开始调用foo函数后得到4；4.打印得到的4
# print("-"*20)   # 5.打印20个分隔线
# print("two", next(g))  # 6.接着之前return后的代码继续执行，直执行到yield

# 8.exec函数的用法：执行储存在字符串或文件中的 Python 语句
# 语法：exec(object[, globals[, locals]])
# a = [1, 2]
# exec('print(a[0])')     # 单行语句
# 多行语句
exec("""                
for i in range(3):
    print(i)
""")



