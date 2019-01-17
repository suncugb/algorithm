# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Leo'


class Node(object):
	"""
	定义链表的Node节点。
	"""

	def __init__(self, data, next=None):
		'''
		Node节点的初始化方法。

		参数：
			data：存储数据。
			next：下一个Node节点的引用地址。
		'''
		self.__data = data
		self.__next = next
	
	@property
	def data(self):
		'''
		获取Node节点的存储数据。

		返回：
			当前Node节点存储的数据。
		'''
		return self.__data

	@data.setter
	def data(self, data):
		'''
		设置Node节点的存储数据。
		'''
		self.__data = data

	@property
	def next(self):
		'''
		获取Node节点存储的下一个节点的引用地址。
		'''
		return self.__next

	@next.setter
	def next(self, next):
		'''
		设置Node节点存储下一个节点的引用地址。

		参数：
			next：下一个Node节点的引用地址。
		'''
		self.__next = next

class SinglyLinkedList(object):
	"""单链表。"""
	def __init__(self):
		'''
		单链表初始化。
		'''
		self.__head = None

	def insert_to_head(self, value):
		'''
		在链表的头部插入一个存储value数据的Node节点。

		参数：
			value：将要存储的数据。
		'''
		node = Node(value)
		node.next = self.__head
		self.__head = node

	def insert_before(self, node, value):
		'''
		在指定的Node节点前插入一个存储value数据的Node节点。

		参数：
			node：指定的Node节点。
			value：将要存储在新节点中的数据。
		'''
		# 当节点为空或头节点为空时直接返回
		if node == None or self.__head == None: 
			return

		# 当指定的Node节点为头节点且头节点不为空时，直接插入在头节点前
		if node == self.__head:
			self.insert_to_head(value)
			return

		new_node = Node(value)
		start = self.__head
		not_found = False
		while start.next != node:
			if start.next == None:
				not_found = True
				break
			else:
				start = start.next
		if not_found == False:
			new_node.next = node
			start.next = new_node

	def insert_after(self, node, value):
		'''
		在指定的Node节点后插入一个存储value数据的Node节点。

		参数：
			node：指定的Node节点。
			value：将要存储在新节点中的数据。
		'''
		# 节点为空直接返回
		if node == None:
			return

		new_node = Node(value)
		new_node.next = node.next
		node.next = new_node
			
	def delete_by_node(self, node):
		'''
		删除指定的Node节点。
		
		参数：
			node：要删除的Node节点。
		'''
		# 节点为空则直接返回
		if node == None:
			return 
		# 当指定的Node节点是头节点
		if node == self.__head:
			self.__head = node.next
			return
		
		start = self.__head
		not_found = False
		while start.next != node:
			if start.next == None:
				not_found = True
				break
			else:
				start = start.next
		if not_found == False:
			start.next = node.next

	def delete_by_value(self, value):
		'''
		删除指定存储数据的Node节点。
		'''
		# 当头节点为空时直接返回
		if self.__head == None:
			return

		# 当删除的节点为头节点时
		if self.__head.data == value:
			self.__head = self.__head.next

		start = self.__head
		node = self.__head.next
		not_found = False
		while node.data != value:
			if node.next == None:
		 		not_found = True
		 		break
		 	else:
		 		start = node
		 		node = node.next
		if not_found == False:
		 	start.next = node.next

	def delete_last_N_node(self, n):
		'''
		删除链表中倒数第N个节点。
		'''
		if n == None:
			return

		if n == 1 and self.__head == None:
			return





			