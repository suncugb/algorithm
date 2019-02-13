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

class SinglyLinkedList(object):
	"""单链表。"""
	def __init__(self):
		'''
		单链表初始化。
		'''
		self.__head = None

	def get_head(self):
		'''
		获取链表head节点。

		返回：
			head节点。
		'''
		return self.__head

	def set_head(self,node):
		'''
		设置指定node为链表的head节点。

		参数：
			node：指定节点。
		'''
		self.__head = node

	def insert_to_head(self, value):
		'''
		在链表的头部插入一个存储value数据的Node节点。

		参数：
			value：将要存储的数据。
		'''
		if self.__head == None:
			return

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
		#当节点为空或头节点为空时直接返回
		if node == None or self.__head == None: 
			return

		#当指定的Node节点为头节点且头节点不为空时，直接插入在头节点前
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
		#节点为空直接返回
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
			True或False。
		'''
		#节点为空则直接返回
		if node == None:
			return False

		#当删除的Node节点是头节点
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
			True或False。
		'''
		#当头节点为空时直接返回
		if self.__head == None:
			return False

		#当删除的节点为头节点时
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
		返回：
			True或False。
		'''
		fast = self.__head
		slow = self.__head
		if fast == None or slow == None:
			return False
		
		step = 0
		while step < n:
			fast = fast.next
			step += 1

		cur = slow
		while fast.next != None:
			cur = slow
			fast = fast.next
			slow = slow.next

		if cur == self.__head: 		#倒数第N个节点正好是头节点时要特殊处理	
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
		node = self.__head
		if node == None:
			return None

		while node:
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

		while node:
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

		while fast.next:
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
		#当为链表为空或只有一个head节点时，无需反转（即链表至少有2个以上节点才需要反转）
		if self.__head == None or self.__head.next == None:
			return

		prev = self.__head			 
		cur = self.__head.next 		 
		temp = self.__head.next.next 
		while cur:
			temp = cur.next #保存当前节点的下一个节点位置
			cur.next = prev #反转，将当前节点指向前一个节点
			prev = cur 		#指针后移，将前一个节点位置向后移动到当前节点位置
			cur = temp 		#指针后移，将当前节点位置向后移动到其下一个节点位置

		self.__head.next = None #将原链表的head节点指向NULL
		self.__head = prev 		#更新反转后新链表的head节点

	def reversed2(self):
		'''
		链表反转：递归方式
		'''
		pass

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
	l = SinglyLinkedList()

	#test create node
	node = l.create_node('abc')
	l.set_head(node)

	#test insert_to_head operation
	l.insert_to_head(4)
	l.insert_to_head('leo')
	l.insert_to_head('001')
	l.insert_to_head('xxxx')
	l.print_all()

	#test insert_before operation
	l.insert_before(node,88)
	l.print_all()

	#test insert_after operation
	l.insert_after(node,'hello')
	l.print_all()

	#test find operation
	node = l.find_by_value('001')
	print(node.data)

	node = l.find_by_index(2)
	print(node.data)

	node = l.find_middle_node()
	print(node.data)

	#test delete operation
	l.delete_by_value(88)
	l.print_all()

	l.delete_by_node(node)
	l.print_all()

	l.delete_last_N_node(3)
	l.print_all()

	#test reversed
	l.reversed()
	l.print_all()

	#test has_ring
	print(l.has_ring()) #has no ring

	node1 = l.find_by_value('xxxx')
	node2 = l.find_by_value('abc')
	node1.next = node2  #has a ring
	print(l.has_ring())