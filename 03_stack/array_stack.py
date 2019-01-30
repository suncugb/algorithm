# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 基于数组实现的顺序栈。
# 功能：入栈、出栈。
#
# Author：Leo

from __future__ import print_function
from array import Array

class ArrayStack(object):
	"""
	定义栈类。
	"""
	def __init__(self, size):
		'''
		初始化。
		'''
		self.__count = 0			#栈中元素个数
		self.__size = size 			#数组大小 	
		self.__array = Array(size)	#数组

	def push(self, item):
		'''
		入栈操作。

		参数：
			item：待入栈的数据。
		返回：
			True或False。
		'''
		if self.__count == self.__size:				#若数组已满,则入栈失败返回False
			return False

		self.__array.insert(self.__count,item)		#数组未满，则入栈，并返回True
		self.__count += 1							#栈中元素个数加1

		return True 								#入栈成功，返回True

	def pop(self):
		'''
		出栈操作。
		'''
		if self.__count == 0: 						#若栈为空，则直接返回
			return
	
		temp = self.__array.find(self.__count - 1) 	#若栈不为空，则出栈
		self.__count -= 1 							#栈中元素个数减1

		return temp 								#返回出栈元素

	def print_all(self):
		pos = 0
		while pos < self.__count:
			print(str(self.__array.find(pos)) + ',',end='')
			pos += 1
		print('\n')

if __name__ == '__main__':
	s = ArrayStack(5)

	#test push
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.print_all()

	s.push(5)
	s.print_all()

	#test pop
	s.pop()
	s.print_all()

	s.pop()
	s.print_all()
