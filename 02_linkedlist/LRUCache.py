# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 基于单链表的LRU缓存淘汰策略实现。 
# LRU：Least Recently Used。
# 思路：
# 每当访问一个新数据时，遍历链表：
# 1.如果链表已经存在该数据，则删除原节点，并将包含新数据的节点插入到表头。
# 2.如果链表中不存在该数据：
# 	1）如果缓存没满，则直接将包含该数据的节点插入到表头。
#	2）如果缓存已满，则删除尾节点，并将包含该数据的节点插入到表头。
# 
# Author：Leo

from __future__ import print_function
from singlyLinkedList import SinglyLinkedList

class LRU(object):
	"""
	定义LRU类。
	"""
	def __init__(self):
		'''
		初始化。
		'''
		self.__cache = SinglyLinkedList()
		self.__maxCacheSize = 5

	def __len(self):
		'''
		获取缓存的大小。
		'''
		head = self.__cache.get_head()
		pos = 0
		while head:
			head = head.next
			pos += 1

		return pos

	def __add(self, data):
		'''
		将数据加入到缓存。
		'''
		head = self.__cache.get_head()
		if head:
			self.__cache.insert_to_head(data)
		else:
			self.__cache.set_head(self.__cache.create_node(data))

	def __remove(self, prev, current):
		'''
		从缓存删除指定节点。

		参数：
			prev：待删除节点的前一个节点地址。
			current：待删除节点。
		'''
		prev.next = current.next

	def __is_exist(self, data):
		'''
		判断缓存中是否存在指定数据。

		参数：
			data：指定数据，即访问的新数据。
		返回：
			is_exist,旧节点的前一个节点，旧节点。
		'''
		head = self.__cache.get_head()
		prev = None 
		is_exist = False
		while head:
			if head.data == data:
				is_exist = True
				break
			else:
				prev = head
				head = head.next

		return is_exist,prev,head

	def __is_full(self):
		'''
		判断缓存是否已满。
		返回：
			True或False。
		'''
		if self.__len() + 1 < self.__maxCacheSize:
			return False
		else:
			return True

	def update(self, data):
		'''
		根据LRU策略更新缓存。

		参数：
			data：访问的新数据。
		'''
		#判断访问的新数据是否存在
		is_exist,prev,oldnode = self.__is_exist(data)
		#存在，则删除旧节点，在插入新节点到头节点前
		if is_exist:
			self.__remove(prev,oldnode)	
			self.__add(data)			
		#不存在
		else:
			#缓存已满，则删除尾节点，在插入新节点到头节点前
			if self.__is_full():
				head = self.__cache.get_head()
				prev_tail = None
				tail = None
				while head:
					if head.next.next == None:
						prev_tail = head
						tail = head.next
						break
					else:
						head = head.next

				prev_tail.next = None 	
				self.__add(data)	
			#缓存未满，则直接插入新节点到头节点前	
			else:
				self.__add(data)	

	def print_all(self):
		'''
		打印缓存的所有数据。
		'''
		head = self.__cache.get_head()
		if head == None:
			print('当前链表没有数据！')
			return 

		while head:
			print(str(head.data) + '->',end='')
			head = head.next
		print('\n')

if __name__ == '__main__':
	lru_cache = LRU()
	lru_cache.update(4)
	lru_cache.update('leo')
	lru_cache.update('hello')
	lru_cache.update('world')
	lru_cache.update('xxxx')
	lru_cache.print_all()

	lru_cache.update(88)
	lru_cache.print_all()

	lru_cache.update('start')
	lru_cache.print_all()
