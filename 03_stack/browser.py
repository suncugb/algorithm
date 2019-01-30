# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 基于栈实现浏览器的前进和后退功能。
# 思路：使用两个栈x，y，x用来首先保存浏览的页面。
# 1）点击后退时，将x栈顶页面取出，并保存到y栈中，当x栈为空时，无法继续后退。
# 2）点击前进时，将y栈顶页面取出，并保存到x栈中，当y栈为空时，无法继续前进。
# 
# Author：Leo

from __future__ import print_function
from linked_stack import LinkedStack

class Browser(object):
	"""
	定义浏览器类。
	"""
	def __init__(self):
		'''
		初始化。
		'''
		self.__stack_x = LinkedStack(5)
		self.__stack_y = LinkedStack(5)

	def open(self, url):
		'''
		访问新页面。
		'''
		print("Open new url %s" % url, end="\n")
		self.__stack_x.push(url)

	def forward(self):
		'''
		前进。
		'''
		top = self.__stack_y.pop()
		if top:
			self.__stack_x.push(top.data)
			print("from %s forward to %s" % (self.__stack_x.head.next.data,top.data), end="\n")
		else:
			print('can not to forward!')

	def back(self):
		'''
		后退。
		'''
		top = self.__stack_x.pop()
		if top:
			self.__stack_y.push(top.data)
			print("from %s back to %s" % (top.data,top.next.data), end="\n")
		else:	
			print('can not to back!')

	def clear(self):
		'''
		清空栈。
		'''
		self.__stack_y.clear()

	def print_all(self):
		'''
		打印栈中所有元素。
		'''
		self.__stack_x.print_all()
		self.__stack_y.print_all()

if __name__ == '__main__':
	browser = Browser()

	#test open
	browser.open('www.baidu.com')
	browser.open('www.sina.com')
	browser.open('www.google.com')
	# browser.print_all()

	#test back
	browser.back()
	browser.back()
	# browser.print_all()

	#test forword
	browser.forward()
	browser.forward()
	# browser.print_all()