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

### No278.第一个错误的版本(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No167.两数之和II-输入有序数组](https://leetcode-cn.com/problems/first-bad-version/)  
>你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。  
>假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。  
>你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

3. 示例:
    1. 示例1:
    ```
给定 n = 5，并且 version = 4 是第一个错误的版本。
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。 
    ```
4. 思路:  
>不能写 int mid = (l + r) / 2; 要写 int mid = l + (r - l) / 2;  
>这个题目，返回 l 或者 r 都行，因为终止条件是 l == r.  
>这是二分里比较难的题目了吧，找的是分割点，不是某个值。
> * [\*\*\*\*\*\*\*\*########] 就像这样的有序数组，找第一个 # 号。
> * 二分搜索的演化版本，查找某个值，返回其索引，如果找不到，返回其本来应该所在的位置（比如上面 # 号的位置）。遇到这种二分搜索，就拿这个 bad version 来套就行了

5. 题解:
```java
public class Solution extends VersionControl {
        public int firstBadVersion(int n) {
            int l = 1;
            int r = n;
            int mid;
            while(l<r){
                mid = l+(r-l)/2;
                if (isBadVersion(mid)) {
                    r = mid;
                } else {
                    l = mid+1;
                }
            }
            return l;
        }
}
```

### No349.两个数组的交集(简单)
1. 难度:<font color=green>简单<font color=green>
2. [题目:No349.两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays/)  
>给定两个数组，编写一个函数来计算它们的交集。

3. 示例:
    1. 示例1:
    ```
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
    ```
    2. 示例2:
    ```
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
    ```
4. 说明:
* 输出结果中的每个元素一定是唯一的。
* 我们可以不考虑输出结果的顺序。
5. 思路:  
>先将nums1放进map中去重,然后向map2放入nums2和nums1的交集数据,然后取出放入数组中返回

6. 题解:
```java
public int[] intersection(int[] nums1, int[] nums2) {
        if (nums1 == null || nums2 == null) {
            return null;
        }
        Map<Integer,Integer> map1 = new HashMap<>();
        for (int value : nums1) {
            map1.put(value, 0);
        }
        Map<Integer,Integer> map2 = new HashMap<>();
        for (int value : nums2) {
            if (map1.get(value) !=null && map2.get(value) == null) {
                map2.put(value, 0);
            }
        }
        Set<Integer> set = map2.keySet();
        int[] res = new int[set.size()];
        int i =0;
        for(Integer v : set){
            res[i] = v;
            i++;
        }
        return res;
}
```

## 二、中等题
### No74.搜索二维矩阵(中等)
1. 难度:<font color=orange>中等<font color=orange>
2. [题目:No74.搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)  
>编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
> * 每行中的整数从左到右按升序排列。
> * 每行的第一个整数大于前一行的最后一个整数。

3. 示例:
    1. 示例1:
    ```
1 ,3 ,5 ,7
10,11,16,20
23,30,34,60
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
    ```
    2. 示例2:
    ```
1 ,3 ,5 ,7
10,11,16,20
23,30,34,60
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
    ```
4. 提示：  
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 100
* -104 <= matrix\[i\]\[j\], target <= 104
5. 思路:  
> 注意到输入的 m x n 矩阵可以视为长度为 m x n的有序数组。    
> 由于该虚数组的序号可以由下式方便地转化为原矩阵中的行和列 (我们当然不会真的创建一个新数组) ，该有序数组非常适合二分查找。  
> row = idx / n ， col = idx % n。

6. 题解:
```java
public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) return false;
        int n = matrix[0].length;

        // 二分查找
        int left = 0, right = m * n - 1;
        int pivotIdx, pivotElement;
        while (left <= right) {
            pivotIdx = (left + right) / 2;
            pivotElement = matrix[pivotIdx / n][pivotIdx % n];
            if (target == pivotElement) return true;
            else {
            if (target < pivotElement) right = pivotIdx - 1;
            else left = pivotIdx + 1;
            }
        }
        return false;
}
```

### No275.H指数II(中等)
1. 难度:<font color=orange>中等<font color=orange>
2. [题目:No275.H指数II](https://leetcode-cn.com/problems/h-index-ii/)  
>给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。  
> h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"  
3. 示例:
    ```
示例:
输入: citations = [0,1,3,5,6]
输出: 3 
解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。
    ```
4. 说明:如果 h 有多有种可能的值 ，h 指数是其中最大的那个。
5. 进阶：
* 这是 H 指数 的延伸题目，本题中的 citations 数组是保证有序的。
* 你可以优化你的算法到对数时间复杂度吗？
6. 思路:  
>二分法开始查找,如果找到值和length-下标对应上的,那么这个length-mid必是答案  
>如果没对应上,继续查找直到退出循环,length-l就是答案

7. 题解:
```java
private static int hIndex(int[] citations) {
        int l=0;
        int length=citations.length;
        int r=length-1;
        int mid;
        while (l<=r){
            mid = l+(r-l)/2;
            if (citations[mid]==length-mid) {
                return length-mid;
            } else if (citations[mid]>length-mid){
                r = mid-1;
            } else {
                l = mid+1;
            }
        }
        return length-l;
}
```

### No540.有序数组中的单一元素(中等)
1. 难度:<font color=orange>中等<font color=orange>
2. [题目:No540.有序数组中的单一元素](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)  
>给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。  
3. 示例:
    1. 示例1:
    ```
输入: [1,1,2,3,3,4,4,8,8]
输出: 2
    ```
4. 注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
5. 思路:  
>每次寻找中位数后判断前后是否有相同的数字,有的话排除这两个数字,根据左右两边剩余长度的奇偶来判断单个数字在左边还是右边  
6. 题解:
```java
public int singleNonDuplicate(int[] nums) {
    int lo = 0;
    int hi = nums.length - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        boolean halvesAreEven = (hi - mid) % 2 == 0;//判断右边是奇数还是偶数 true为右边奇数,false为右边偶数
        if (nums[mid + 1] == nums[mid]) {
            if (halvesAreEven) {
                lo = mid + 2;
            } else {
                hi = mid - 1;
            }
        } else if (nums[mid - 1] == nums[mid]) {
            if (halvesAreEven) {
                hi = mid - 2;
            } else {
                lo = mid + 1;
            }
        } else {
            return nums[mid];//没找到相同的数字,该数字就是单个的数字
        }
    }
    return nums[lo];
}
```