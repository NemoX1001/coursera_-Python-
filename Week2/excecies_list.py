#有一个咖啡列表['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']，列表中每一个元素都是由咖啡名称、价格和一些其他非字母字符组成，编写一个函数clean_list()处理此咖啡列表，处理后列表中只含咖啡名称，并将此列表返回。__main__模块中初始化咖啡列表，调用clean_list()函数获得处理后的咖啡列表，并利用zip()函数给咖啡名称进行编号后输出，输出形式如下：
#1 Latte
#2 Americano
#3 Cappuccino
#4 Mocha

def clean(s1):
	s2 = []
	for item in s1:
		for ch in item:
			if ch.isalpha() != True:
				item = item.replace(ch,"")
		s2.append(item)
	return s2

s = ['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
s2 = clean(s)
print (s2)
