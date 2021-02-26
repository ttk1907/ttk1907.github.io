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
## 一、简单题练手
### No35.搜索插入位置(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No35.搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)  
>给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
>你可以假设数组中无重复元素。

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
4. 思路:  
> 正常二分查找即可,如果找不到,left指针正好就是待插入的位置

5. 题解:
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

### No69.X的平方根(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No69.X的平方根](https://leetcode-cn.com/problems/sqrtx/)

>实现 `int sqrt(int x)` 函数。
>计算并返回 x 的平方根，其中 x 是非负整数。
>由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

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
4. 思路:

> 由于 x 平方根的整数部分是满足 k^2 <=x 的最大 k 值，因此我们可以对 k 进行二分查找，从而得到答案。
>下限l设为0,上限r设为x,每次取中间的数mid平方后和x比较
>   * 小于<=x的话,l=mid+1
>   * 大于x的话,r=mid-1

5. 题解:
```java
public int mySqrt(int x) {
        int l = 0, r = x, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if ((long) mid * mid <= x) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans;
}
```

### No167.两数之和II-输入有序数组(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No167.两数之和II-输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

>给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
>函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
>你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

3. 示例:
    1. 示例1:
    ```
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
    ```
    2. 示例2:
    ```
输入：numbers = [2,3,4], target = 6
输出：[1,3]
    ```
    3. 示例3:
    ```
输入：numbers = [-1,0], target = -1
输出：[1,2]
    ```
4. 提示:
* 2 <= numbers.length <= 3 * 104
* -1000 <= numbers[i] <= 1000
* numbers 按 递增顺序 排列
* -1000 <= target <= 1000
* 仅存在一个有效答案

5. 思路:

>循环每一个数,然后用二分法找出另一个数字
>这道题也可以使用双指针,l=0,r=length-1,通过加和判断与目标的大小求出答案

6. 题解:
```java
private static int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        int t;
        for (int i=0;i<numbers.length;i++){
                res[0] = i+1;
                //二分查找成功
                t = binarySearch(res[0],numbers,target-numbers[i]);
                if (t!=-1){
                        res[1] = t+1;
                        break;
                }
        }
        return res;
}

private static int binarySearch(int l, int[] numbers, int target){
        int r = numbers.length-1;
        int mid;
        while (l<=r){
                mid = l+(r-l)/2;
                if (numbers[mid] == target) {
                        return mid;
                } else if (numbers[mid]>target){
                        r = mid-1;
                } else {
                        l = mid+1;
                }
        }
        return -1;
}
```