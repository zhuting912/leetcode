#! usr/bin/env python
# -*- coding:utf-8 -*-

'''
Problem 1 : Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a special target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
给定一个整数数组，返回加和为特定值的两个数的下标。
假设有唯一解，并且一个元素不能使用两次。
'''


def twoSum(nums, target):
    '''
    :param nums: List[int]
    :param target: int
    :return: List[int]
    '''
    dict = {}
    for i, element in enumerate(nums):
        if element in dict:
            return [dict[element], i]
        else:
            dict[target - element] = i