---
layout: post
title:  "数据结构与算法04-高级算法"
date:   2021-02-22
categories: study
tags: DataStructureAndAlgorithm
---

* content
{:toc}

1. 二分查找算法(非递归)
2. 分治算法
3. 动态规划
4. KMP算法
5. 贪心算法
6. 普利姆算法(Prim)
7. 克鲁斯卡尔算法(Kruskal)
8. 迪杰斯特拉算法(Dijkstra)
9. 弗洛伊德算法(Floyd)
10. 马踏棋盘算法




# 一、程序员常用10种算法

## 1.二分查找算法(非递归)
1. 二分查找算法(非递归)介绍
    1. 前面我们讲过了二分查找算法,是使用递归的方式,下面我们讲解二分查找算法的非递归方式
    2. 二分查找法只适用于从有序的数列中进行查找(比如数字和字母等),将数列排序后再进行查找
    3. 二分查找法的运行时间为对数时间 O(㏒₂n) ,即查找到需要的目标位置最多只需要 ㏒₂n 步, 假设从[0,99]的队列(100 个数, 即 n=100)中寻到目标数 30,则需要查找步数为 ㏒₂100 , 即最多需要查找 7 次( 2^6 < 100 < 2^7)   
2. 二分查找代码
```java
public static int binarySearch(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;
    while(left <= right) { //说明继续查找 
        int mid = (left + right) / 2; 
        if(arr[mid] == target) {
            return mid;
        } else if ( arr[mid] > target) {
            right = mid - 1;//需要向左边查找
        } else {
            left = mid + 1; //需要向右边查找
        }
    }
    return -1;
}
```

## 2.分治算法
## 3.动态规划算法
## 4.KMP算法
## 5.贪心算法
## 6.普里姆算法
## 7.克鲁斯卡尔算法
## 8.迪杰斯特拉(Dijkstra)算法
## 9.弗洛伊德算法
## 10.马踏棋盘算法