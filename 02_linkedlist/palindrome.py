# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 回文字符串判断。
#
# Author:Leo

from singlyLinkedList import SinglyLinkedList

def reversed(head):
	'''
	根据指定的head节点反转链表。

	参数：
		head：链表头节点。
	返回：
		反转后新链表的head节点（即原链表的尾节点）。
	'''
 	pre = None
 	while head:
 		temp = head.next
 		head.next = pre
 		pre = head
 		head = temp

 	return pre 

def is_palindrome(l):
	'''
	回文字符串检测。

	参数：
		l：待检测的单链表。
	返回：
		True或False。
	'''
	fast = l.get_head()
	slow = l.get_head()
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	new_head = reversed(slow) #返回反转后新链表的head节点
	old_head = l.get_head()	  #原链表的head节点
	while old_head and new_head:
		if old_head.data == new_head.data:
			old_head = old_head.next
			new_head = new_head.next
		else:
			return False

	return True

if __name__ == '__main__':
	test_str_array = ['ab', 'aa', 'aba', 'abba', 'abcba']
	for s in test_str_array:
		l = SinglyLinkedList()
		for i in s:
			l.insert_to_head(i)
		l.print_all()
		print(is_palindrome(l))