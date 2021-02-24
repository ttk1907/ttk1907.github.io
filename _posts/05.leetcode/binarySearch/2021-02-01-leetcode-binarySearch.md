---
layout: post
title:  "二分查找题型笔记"
date:   2021-02-01
categories: leetcode
tags: leetcode
---

* content
{:toc}

1. 二分查找题型笔记




# 一、二分查找题型笔记

## No35.搜索插入位置(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No35.搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)
    - 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    - 你可以假设数组中无重复元素。
3. 示例:
    1. 示例1:   
    ```
输入: [1,3,5,6], 5
输出: 2
    ```
    2. 示例2:   
    ```
输入: [1,3,5,6], 2
输出: 1
    ```
    3. 示例3:   
    ```
输入: [1,3,5,6], 7
输出: 4
    ```
    4. 示例4:   
    ```
输入: [1,3,5,6], 0
输出: 0
    ```
5. 思路:正常二分查找即可,如果找不到,left指针正好就是待插入的位置
6. 我的解答:
```java
public int searchInsert(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    while(left <= right) { //说明继续查找
        int mid = (left + right) / 2;
        if(nums[mid] == target) {
            return mid;
        } else if ( nums[mid] > target) {
            right = mid - 1;//需要向左边查找
        } else {
            left = mid + 1; //需要向右边查找
        }
    }
    return left;
}
```

## No69.X的平方根(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No69.X的平方根](https://leetcode-cn.com/problems/sqrtx/)
    - 实现 `int sqrt(int x)` 函数。
    - 计算并返回 x 的平方根，其中 x 是非负整数。
    - 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
3. 示例:
    1. 示例1:
    ```
输入: 4
输出: 2
    ```
    2. 示例2:
    ```
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
    ```





