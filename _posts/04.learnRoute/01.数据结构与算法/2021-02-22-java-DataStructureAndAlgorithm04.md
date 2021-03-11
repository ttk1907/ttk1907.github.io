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
1. 分治算法介绍
    1. 分治法是一种很重要的算法。 字面上的解释是“分而治之” ，就是把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题……直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。 这个技巧是很多高效算法的基础， 如排序算法(快速排序，归并排序)，傅立叶变换(快速傅立叶变换)……
    2. 分治算法可以求解的一些经典问题 : 二分搜索、大整数乘法、棋盘覆盖、合并排序、快速排序、线性时间选择、最接近点对问题、循环赛日程表、汉诺塔
2. 分治算法的基本步骤
分治法在每一层递归上都有三个步骤：
    1. 分解：将原问题分解为若干个规模较小，相互独立，与原问题形式相同的子问题
    2. 解决：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题
    3. 合并：将各个子问题的解合并为原问题的解。
3. 分治(Divide-and-Conquer(P))算法设计模式如下：  
![分值算法设计](/assets/01.java提升计划/01.数据结构与算法/04/分值算法设计.jpg)
4. 分治算法最佳实践-汉诺塔
    1. 汉诺塔的传说： 汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着 64 片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。 并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
    2. 思路分析:
        1. 如果是有一个盘， A->C
        2. 如果我们有 n >= 2 情况，我们总是可以看做是两个盘,最下边的盘和上面的盘
            1. 先把最上面的盘 A->B
            2. 把最下边的盘 A->C
            3. 把 B 塔的所有盘 从 B->C  
    3. 代码实现:
    ```java
public static void main(String[] args) {
        HanoiTower(5,'A','B','C');
}
private static void HanoiTower(int num, char a, char b, char c){
        if (num == 1){
            System.out.println(num+"号盘子: "+a+" -> "+c);
        } else {
            HanoiTower(num-1,a,c,b);//把多余的盘子由A->B
            System.out.println(num+"号盘子: "+a+" -> "+c);//把最大的由A->C
            HanoiTower(num-1,b,a,c);//把剩下的由B->C
        }
}
    ```

## 3.动态规划算法
1. 一道题目:有2,5,7三种硬币,现在要组成27元,问最少的硬币组合是多少枚
2. 动态规划四个步骤
    1. 确定状态：
        * 最后一步(最优策略中使用的最后一枚硬背ak)
        * 转化成子问题(最少的硬币拼出更小的面值27-ak)
    2. 转移方程:
        * f[x] = min{f[x-2]+1,f[x-5]+1,f[x-7]+1}
    3. 初始化和边界情况
        * f[0]=0,如果不能拼出Y,f[x]=-1
    4. 计算顺序
        * f[0],f[1],f[2],f[3]
3. 题解:
```java
public static int minCoin(int num) {
        int[] dp = new int[num + 1];
        dp[0] = 0;
        for (int i = 1; i < num + 1; i++) {
            dp[i] = Math.min(array(i - 2,dp), Math.min(array(i - 5,dp), array(i - 7,dp))) + 1;
        }
        return dp[num];
}
public static int array(int i,int[] dp) {
        if (i < 0) {
            return Integer.MAX_VALUE - 1;
        }
        return dp[i];
}
```



## 4.KMP算法
## 5.贪心算法
## 6.普里姆算法
## 7.克鲁斯卡尔算法
## 8.迪杰斯特拉(Dijkstra)算法
## 9.弗洛伊德算法
## 10.马踏棋盘算法