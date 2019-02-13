# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 带哨兵节点的单链表。
#
# Author:Leo

from __future__ import print_function

class Node(object):
	"""
	定义单链表的Node节点。
	"""
	def __init__(self, data, next=None):
		'''
		Node节点的初始化。

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

class SentinelSinglyLinkedList(object):
	"""带哨兵节点的单链表。"""
	def __init__(self):
		'''
		单链表初始化。
		'''
		self.__head = Node(None)

	@property
	def head(self):
		'''
		获取head节点。
		'''
		return self.__head

	def add(self, value):
		'''
		从链表头部插入。
		'''
		new_node = Node(value)
		new_node.next = self.__head
		self.__head = new_node

	def append(self, value):
		'''
		从尾部插入。
		'''
		cur = self.__head
		while cur.next:
			cur = cur.next

		new_node = Node(value)
		cur.next = new_node

	def insert_before(self, node, value):
		'''
		在指定node节点前插入。
		'''
		if node == self.__head: #当指定节点是头节点时要特殊处理
			self.add(value) 	#在头部插入并更新头节点
			return 

		prev = self.__head
		cur = self.__head

		while cur:
			if cur.data == node.data:
				break
			else:
				prev = cur
				cur = cur.next

		new_node = Node(value)
		prev.next = new_node
		new_node.next = node

	def insert_after(self, node, value):
		'''
		在指定node节点后插入。
		'''
		new_node = Node(value)
		new_node.next = node.next
		node.next = new_node
			
	def delete_by_node(self, node):
		'''
		删除指定的Node节点。
		
		参数：
			node：要删除的Node节点。
		返回：
			True或False。
		'''
		if node == self.__head: 	#待删除节点正好是头节点时要特殊处理
			self.__head = node.next #更新头节点
			return 

		prev = None
		cur = self.__head
		while cur:
			if cur.data == node.data:
				break
			else:
				prev = cur
				cur = cur.next

		prev.next = node.next

	def delete_last_N_node(self, n):
		'''
		删除链表中倒数第N个节点。

		思路：
			设置快、慢指针，快指针先走N步后，慢指针开始移动，最后当快指针走到链尾时，慢指针指向的Node节点即为倒数第N个节点。
		
		参数：
			n：需要删除的倒数第N个序数。
		返回：
			True或False。
		'''
		fast = self.__head
		slow = self.__head

		step = 0
		while step < n:
			fast = fast.next
			step += 1

		cur = slow
		while fast.next:
			cur = slow
			fast = fast.next
			slow = slow.next

		if cur == self.__head:		#倒数第N个节点正好是头节点时要特殊处理	
			self.__head = cur.next 	#更新头节点
		else:
			cur.next = slow.next
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
		cur = self.__head

		while cur:
			if cur.data == value:
				return cur
			else:
				cur = cur.next 

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
		cur = self.__head
		pos = 0

		while cur:
			if pos == index:
				return cur
			else:
				cur = cur.next
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
	
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		return slow

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

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				return True

		return False
	
	def reversed(self):
		'''
		链表反转：非递归方式。
		'''		
		prev = None
		cur = self.__head
		temp = self.__head.next
		while cur:
			temp = cur.next
			cur.next = prev
			prev = cur
			cur = temp

		self.__head = prev 		#更新反转后新链表的head节点

	def print_all(self):
		'''
		打印当前链表的所有节点数据。
		'''
		cur = self.__head
		while cur:
			print(str(cur.data) + '->',end='')
			cur = cur.next
		print('\n')

if __name__ == '__main__':
	l = SentinelSinglyLinkedList()

	#test add operation
	l.add(4)
	l.add('leo')
	l.add('001')
	l.add('xxxx')
	l.add('abc')
	l.print_all()

	#test append operation
	l.append('come')
	l.append('to')
	l.append('2019')
	l.print_all()

	#test insert_before operation
	node = l.find_by_value('to')
	l.insert_before(node,88)
	l.print_all()

	#test insert_after operation
	l.insert_after(node,'hello')
	l.print_all()

	#test find operation
	node = l.find_by_value('hello')
	print(node.data)

	node = l.find_by_index(2)
	print(node.data)

	node = l.find_middle_node()
	print(node.data)

	#test delete operation
	l.delete_by_node(node)
	l.print_all()

	l.delete_last_N_node(5)
	l.print_all()

	l.delete_last_N_node(8)
	l.print_all()

	#test reversed
	l.reversed()
	l.print_all()

	#test has_ring
	print(l.has_ring()) #has no ring

	node1 = l.find_by_value('come')
	node2 = l.find_by_value('hello')
	node1.next = node2  #has a ring
	print(l.has_ring())