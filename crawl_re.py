'''
\w 匹配一个任意字母数字下划线
\W 匹配任意字母数字下划线之外的一个字符
\d 匹配任意一个十进制数
\D 匹配除十进制数之外的任意一个字符
\s 匹配任意一个空白字符
\S 匹配除空白字符之外的任意一个其他字符


 . 匹配除换行符之外的任意字符
 ^ 匹配字符串开始位置 除非在方括号表达式中使用，此时它表示不接受该字符集合
 $ 匹配字符串结束为止
 * 匹配0次或1次或多次前面的原子
 ？匹配0次或1次前面的原子
 + 匹配1次或多次
 {n} 前面原子刚好出现n次
 {n,} 前面原子至少出现n次
 {n,m} 前面的原子出现n-m次
 | 模式选择
 （） 模式单元

 模式修正 re.
 I  匹配忽略大小写
 M 多行匹配
 L 做本地化识别匹配
 U 根据Unicode 字符及解析字符
 S 让.能够匹配换行符

 P.*y 贪婪模式
 P.*?y 懒惰模式
 
'''
import re
pattern1='hp.*y'
pattern2='hp.*?y'

string='abcdfphp2345ypythony_py'
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)#mathc 从头开始匹配
                                  #search 整个
                                 #sub 查找 替换
print(result1)
print(result2)
print(result1.group())
