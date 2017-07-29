#拼接
##不可以使用str + 2 这样的形式来拼接字符串,否则会报类型错误
print('some ' 'example1')
print('some%s' % 'example2')
s = 'some{}'
print(s.format('example3'))
#转义
print('\'some\' example4')
print('''some "e"xampl'e'5''')
#用r防止转义start
print(r'\n\r\t')
print('some\n exam\tple6')
#end
#加\ 可以阻止把回车认成一行
print('''\
some
example\
''')
#用*标识拼接重复次数 
print(3*"some")
print(2*"some" + " example")
#根据下标检索 负数从右边开始 
example = "some example"
print(example[1])
print(example[-1])
print("切片,起始位置和长度:" + example[0:4])
print("从第四个到末尾:" + example[4:])
print("获取前四个:" + example[:4])
#python会处理没有意义的切片,下标超出长度取长度为值
#上边界超长则返回空字符串
print("右侧超长:" + example[4:25535])
print("左侧超长:" + example[25535:])
#字符串不可通过下标来改变已有数值
#example[0] = 2 会报异常
print("长度:%s" % (len(example)))
#返回字符串是否以指定后缀结尾
print(example.endswith("some",0,4))#true
print(example.endswith("some",0,6))#false
#列表
squares = [1,2,3,4,5]
print(squares)
#和字符串一样可以索引和切片
#切片返回的都是新列表,使用切片返回的是浅拷贝副本
print("浅拷贝:%s" % (squares[:]))
#列表可直接链接
print("链接列表:%s" % (squares + [6,7]))
#列表是可变的,可根据下标修改元素
squares[2] = 6
print("修改列表:%s" % (squares))
#使用append方法添加到末尾
squares.append(6)
print("append方法:%s" % (squares))
#对切片赋值来从区块内改变列表 可增加列表本身长度
squares[2:len(squares)] = [3,4,5,6]
print("切片改变:%s" % squares)
#嵌套列表
a1 = [1,2]
a2 = [3,4]
print([a1,a2])