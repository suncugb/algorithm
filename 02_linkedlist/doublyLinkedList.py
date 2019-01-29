# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 1.创建节点：create_node。
# 2.链表插入：insert_to_head、insert_after、insert_before。
# 3.链表删除：delete_by_node、delete_by_value、delete_last_N_node。
# 4.链表查找：find_by_value、find_by_index、find_middle_node。
# 5.链表反转：reversed_self。
# 6.环的检测：has_ring。
#
# Author:Leo

from __future__ import print_function

class Node(object):
	"""
	定义双向链表的Node节点。
	"""
	def __init__(self, data, prev=None, next=None):
		'''
		Node节点初始化。

		参数：
			data：存储数据。
			prev：前一个Node节点的引用地址。
			next：后一个Node节点的引用地址。
		'''
		self.__data = data
		self.__prev = prev
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

		参数：
			data：待设置的数据。
		'''
		self.__data = data

	@property
	def prev(self):
		'''
		获取前一个Node节点的引用地址。
		'''
		return self.__prev

	@prev.setter
	def prev(self, prev):
		'''
		设置前一个Node节点的引用地址。

		参数：
			prev：待设置的引用地址。
		'''
		self.__prev = prev

	@property
	def next(self):
		'''
		获取下一个Node节点的引用地址。
		'''
		return self.__next

	@next.setter
	def next(self, next):
		'''
		设置下一个Node节点的引用地址。

		参数：
			next：待设置的引用地址。
		'''
		self.__next = next

class DoublyLinkedList(object):
	'''
	双向链表。
	'''
	def __init__(self):
		'''
		双向链表初始化。
		'''
		self.__head = None

	def create_node(self, value):
		'''
		根据指定的value创建Node节点。

		参数：
			value：待存储的数据。
		返回：
			Node节点。
		'''
		return Node(value)
	
	def get_head(self):
		'''
		获取head节点。
		'''
		return self.__head

	def set_head(self, head):
		'''
		设置head节点。

		参数：
			head：待设置的节点。
		'''
		if head == None:
			return False

		self.__head = head
		return True

	def insert_to_head(self, value):
		'''
		将Node节点插入到head节点位置。

		参数：
			value：待插入节点存储的数据。
		'''
		if self.__head == None:
			return

		node = Node(value)
		node.prev = None
		node.next = self.__head
		self.__head.prev = node
		self.__head = node

	def insert_before(self, node, value):
		'''
		在指定Node节点前插入新节点。

		参数：
			node：指定的Node节点。
			value：新节点存储的数据。
		'''
		if self.__head == None or node == None:
			return

		if node == self.__head:
			self.insert_to_head(value)
			return 

		new_node = Node(value)
		new_node.prev = node.prev 
		new_node.next = node
		node.prev.next = new_node
		node.prev = new_node

	def insert_after(self, node, value):
		'''
		在指定Node节点后插入新节点。

		参数：
			node：指定的Node节点。
			value：新节点存储的数据。
		'''
		if self.__head == None or node == None:
			return

		new_node = Node(value)
		new_node.prev = node
		new_node.next = node.next
		node.next = new_node

	def delete_by_node(self, node):
		'''
		删除指定的Node节点。

		参数：
			node：待删除的节点。
		'''
		if self.__head == None or node == None:
			return

		node.prev.next = node.next
		node.next.prev = node.prev

	def delete_by_value(self, value):
		'''
		删除存储指定value的Node节点。

		参数：
			value：待删除节点存储的数据。
		'''
		if self.__head == None:
			return

		start = self.__head
		while start:
			if start.data == value:
				start.prev.next = start.next
				start.next.prev = start.prev
				break
			else:
				start = start.next

	def delete_last_N_node(self, n):
		'''
		删除链表中倒数第N个节点。

		思路：
			设置快、慢指针，快指针先走N步后，慢指针开始移动，最后当快指针走到链尾时，慢指针指向的Node节点即为倒数第N个节点。
		
		参数：
			n：需要删除的倒数第N个序数。
		'''
		slow = self.__head
		fast = self.__head

		if slow == None or fast == None:
			return

		pos = 0
		while pos < n:
			fast = fast.next
			pos += 1

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		if slow and slow.prev and slow.next:
			slow.prev.next = slow.next
			slow.next.prev = slow.prev
		else:
			print('N已超过链表最大长度！')

	def find_by_value(self, value):
		'''
		根据指定value查找包含该数据的Node节点。

		参数：
			value：指定的数据。
		返回：
			Node节点。
		'''
		if self.__head == None:
			return

		start = self.__head
		while start:
			if start.data == value:
				break
			else:
				start = start.next

		return start

	def find_by_index(self, index):
		'''
		根据指定索引值查找对应的Node节点。

		参数：
			index：需要查找的Node节点对应的索引值。
		返回：
			Node节点。
		'''
		if self.__head == None:
			return

		pos = 0
		start = self.__head
		while start:
			if pos == index:
				break
			else:
				start = start.next
				pos += 1

		return start

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

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		return slow

	def reversed(self):
		'''
		链表反转：非递归方式。
		'''
		if self.__head == None or self.__head.next == None:
			return

		prev = self.__head
		cur = self.__head.next
		temp = self.__head.next.next
		while cur:
			temp = cur.next
			cur.next = prev
			prev.prev = cur
			prev = cur
			cur = temp

		self.__head.next = None 
		self.__head = prev

	def print_all(self):
		'''
		打印当前链表的所有节点数据。
		'''
		node = self.__head
		if node == None:
			print('当前链表没有数据！')
			return 

		while node:
			print(str(node.data) + '->',end='')
			node = node.next
		print('\n')

if __name__ == '__main__':
	l = DoublyLinkedList()

	#test create node
	node = l.create_node('doublelinkedlist')
	l.set_head(node)

	#test insert_to_head operation
	l.insert_to_head('hello')
	l.insert_to_head(54)
	l.insert_to_head('leo')
	l.insert_to_head('world')
	l.print_all()

	#test insert_before operation
	node = l.find_by_value(54)
	l.insert_before(node,90)
	l.print_all()

	#test insert_after operation
	l.insert_after(node,'xxxx')
	l.print_all()

	#test find operation
	node = l.find_by_value('leo')
	print(node.data)

	node = l.find_by_index(5)
	print(node.data)

	node = l.find_middle_node()
	print(node.data)

	#test delete operation
	l.delete_by_value(90)
	l.print_all()

	l.delete_by_node(node)
	l.print_all()

	l.delete_last_N_node(4)
	l.print_all()

	#test reversed
	l.reversed()
	l.print_all()
