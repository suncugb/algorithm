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
		返回：
			True，成功。
			False，失败。
		'''
		# 节点为空则直接返回
		if node == None:
			return False

		# 当删除的Node节点是头节点
		if node == self.__head:
			self.__head = node.next
			return True
		
		start = self.__head
		not_found = False
		while start.next != node:
			if start.next == None:
				not_found = True
				return False
			else:
				start = start.next
		if not_found == False:
			start.next = node.next

		return True

	def delete_by_value(self, value):
		'''
		删除指定存储数据的Node节点。

		参数：
			value：指定的存储数据。
		返回：
			True，成功。
			False，失败。
		'''
		# 当头节点为空时直接返回
		if self.__head == None:
			return False

		# 当删除的节点为头节点时
		if self.__head.data == value:
			self.__head = self.__head.next
			return True

		start = self.__head
		node = self.__head.next
		not_found = False
		while node.data != value:
			if node.next == None:
		 		not_found = True
		 		return False
		 	else:
		 		start = node
		 		node = node.next
		if not_found == False:
		 	start.next = node.next

		return True

	def delete_last_N_node(self, n):
		'''
		删除链表中倒数第N个节点。

		思路：
			设置快、慢指针，快指针先走N步后，慢指针开始移动，最后当快指针走到链尾时，慢指针指向的Node节点即为倒数第N个节点。
		
		参数：
			n：需要删除的倒数第N个序数。
		参数：
			True，成功。
			False，失败。
		'''
		fast = self.__head
		slow = self.__head
		if fast == None or slow == None:
			return False
		
		step = 0
		while step <= n:
			fast = fast.next
			step += 1

		while fast.next != None:
			current = slow
			fast = fast.next
			slow = slow.next

		current.next = slow.next
		return True

	def find_by_value(self, value):
		'''
		根据指定的数据查找包含该数据的Node节点。

		参数：
			value：指定的数据。
		返回：
			成功，则返回包含指定数据的Node节点。
			失败，则返回空。
		'''
		node = self.__head
		if node == None:
			return None

		while node.next != None:
			if node.data == value:
				return node
			else:
				node = node.next 

		return None

	def find_by_index(self, index):
		'''
		根据指定索引值查找对应的Node节点。

		参数：
			index：需要查找的Node节点对应的索引值。
		返回：
			成功，则返回包含指定数据的Node节点。
			失败，则返回空。
		'''
		node = self.__head
		pos = 0

		if node == None:
			return None

		while node.next != None:
			if pos == index:
				return node
			else:
				node = node.next
				pos += 1

		return None

	def find_middle_node(self):
		'''
		查找链表的中间Node节点。

		思路：
			设置快、慢指针，同时开始移动，快指针每走2步，慢指针走1步，当快指针走到链尾时，慢指针正好走到中间Node节点。

		返回：
			成功，则返回Node节点。
			失败，则返回空。
		'''
		fast = self.__head
		slow = self.__head
		if fast == None or slow == None:
			return None

		while fast.next != None:
			fast = fast.next.next
			slow = slow.next

		return slow

	def create_node(self, value):
		'''
		创建一个存储value值的Node节点。

		参数：
			value：将要存储的数据。
		返回：
			Node节点。
		'''
		return Node(value)

	def has_ring(self):
		'''
		检测链表中是否有环。

		思路：
			设置快、慢指针，同时开始移动，快指针每走2步，慢指针走1步，若快指针与慢指针相遇，则说明有环，否则无环。
		
		返回：
			True：有环。
			False：无环。
		'''
		fast = self.__head
		slow = self.__head

		if fast == None or slow == None:
			return False

		while fast.next != None:
			if fast == slow:
				return True
			else:
				fast = fast.next.next
				slow = slow.next

		return False
	
	def reversed_self(self):
		'''
		链表反转
		'''
		pass
