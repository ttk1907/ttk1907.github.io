---
layout: post
title:  "力扣2021-02月份每日一题"
date:   2021-02-01
categories: leetcode
tags: leetcode
---

* content
{:toc}

1. 力扣2021-02月份每日一题
2. 滑动窗口月




# 一、力扣2021-02月份每日一题

## 02-01:No888.公平的糖果棒交换(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No888.公平的糖果棒交换](https://leetcode-cn.com/problems/fair-candy-swap/)
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。 

因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）  

返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。

3. 示例:
    1. 示例1:   
    ```
输入：A = [1,1], B = [2,2]
输出：[1,2]
    ```
    2. 示例2:   
    ```
输入：A = [1,2], B = [2,3]
输出：[1,2]
    ```
    3. 示例3:   
    ```
输入：A = [2], B = [1,3]
输出：[2,3]
    ```
    4. 示例4:   
    ```
输入：A = [1,2,5], B = [2,4]
输出：[5,4]
    ```

4. 提示:
    * 1 <= A.length <= 10000
    * 1 <= B.length <= 10000
    * 1 <= A[i] <= 100000
    * 1 <= B[i] <= 100000
    * 保证爱丽丝与鲍勃的糖果总量不同。
    * 答案肯定存在。

5. 我的解答:
```java
public int[] fairCandySwap(int[] A, int[] B) {
    int sumA = 0;
    int sumB = 0;
    Map<Integer, Integer> map = new HashMap<>();
    for (int i1 : A) {
        sumA += i1;
    }
    for (int element : B) {
        sumB += element;
        map.put(element, element);
    }
    int temp = (sumA - sumB) >> 1;
    int[] result = new int[2];
    for (int value : A) {
        result[0] = value;
        if (map.get(result[0] - temp)!=null) {
            result[1] = result[0] - temp;
            return result;
        }
    }
    return result;
}
```

6. 官方题解:    
![官方思路](/assets/leetcode/everyProblem/02-01No888公平的糖果棒交换esay.jpg)   
```java
public int[] fairCandySwap(int[] A, int[] B) {
    int sumA = Arrays.stream(A).sum();
    int sumB = Arrays.stream(B).sum();
    int delta = (sumA - sumB) / 2;
    Set<Integer> rec = new HashSet<Integer>();
    for (int num : A) {
        rec.add(num);
    }
    int[] ans = new int[2];
    for (int y : B) {
        int x = y + delta;
        if (rec.contains(x)) {
            ans[0] = x;
            ans[1] = y;
            break;
        }
    }
    return ans;
}
```

## 02-02:No424.替换后的最长重复字符(中等)