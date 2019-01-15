# !/usr/bin/env python
# _*_ coding:utf-8 _*_

#
# 1) insert,delete and random access of array.
# 2) assumes int for element data type.

__author__ = 'Leo'


class Array:
	"""
	define a array class.
	"""

	def __init__(self, capacity):
		'''
		数组类初始化。

		参数：
			capacity：数组的大小。
		'''

		self.__data = []
		self.__capacity = capacity

	def length(self):
		'''
		获取数组的长度。
		'''

		return self.__capacity

	def find(self, index):
		'''
		根据索引查找数据。

		参数：
			index：索引值。

		返回：
			如果索引值越界，则返回False，否则返回找到的数据。
		'''

		if index >= self.__capacity:
			return False
		else:
			return self.__data[index+1]
		
	def delete(self, index):
		'''
		根据索引值删除数据。

		参数：
			index：索引值。

		返回：
			如果索引值越界，则返回False，否则就删除数据并返回True。
		'''

		if index >= self.__capacity:
			return False
		else:
			self.__data.pop(index)
			return True
		
	def insert(self, index, value):
		'''
		在数组中插入数据。

		参数：
			index：插入位置。
			value：数据。

		返回：
			如果索引值越界，则返回False，否则插入数据并返回True。
		'''

		if index >= self.__capacity:
			return False
		else:
			self.__data.insert(index, value)
			return True

	def print_all(self):
		'''
		打印数组中的所有数据。
		'''

		for item in self.__data:
			print(item)

def test():
	array = Array(5)
	array.insert(0, 3)
	# array.insert(0, 99)
	array.insert(1, 4)
	array.insert(2, 5)
 	array.insert(3, 9)
	array.insert(4, 10)
	assert array.insert(0, 100) is True
	assert array.length() == 5
	assert array.find(1) == 4
	assert array.delete(4) is True
	array.print_all()

if __name__ == '__main__':
	test()