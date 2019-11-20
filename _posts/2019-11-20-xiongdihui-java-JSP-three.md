---
layout: post
title:  "Java-JSP第三天"
date:   2019-11-20
categories: Java
tags: Java note
---

* content
{:toc}

1. JSP第3天：重写URL得到Session、EL表达式、EL表达式,取出数据的流程、taglib指令、JSTL标签库








# Java-JSP第三天
## Java--JSP--第3天
### 重写URL得到Session
1. 重写普通的网址,通常是超链接/表单中使用的网址:`url = response.encodeUrl(url);`
2. 重写重定向的网址,这种网址用于重定向:`url = response.encodeRedirectUrl(url);`

### EL表达式
1. 作用:用于快速的从域对象中取出数据,并将结果输出到网页.也可以用于一些运算,运算的结果也会输出到网页
2. 格式:`${表达式}`
3. 例子1:用于计算:`${1+2+3+4+5}`
4. 例子2:用于取出域对象中的数据
    1. 访问存储数据的格式:`${存储的key}`
    2. 访问存储的对象属性值:  

    ```jsp
session.setAttribute("user",new User("admin","123456"));
session.setAttribute("a","username");
静态取值:${存储时的key.属性名}
${user.username}
静态取值:${存储时的key[属性名]}
${user["username"]}
动态取值:${存储时的key[属性名的key]}
${user[a]}  此时输出的是admin
session.setAttribute("a","username");
${user[a]}  此时输出的是123456
    ```

    3. 访问集合/数组中的对象

    ```
静态取值:${存储时的key[下标].属性名}
静态取值:${存储时的key[下标]["属性名]}
动态取值:${存储时的key[下标][属性名的key]}
    ```

### EL表达式,取出数据的流程
1. 取出的顺序:范围从小到大
2. 步骤:
    1. 先从pageContext中寻找数据是否存在
    2. 当pageContext中不存在此数据时,去request中寻找数据是否存在
    3. 当request中不存在此数据时,去session中寻找数据是否存在
    4. 当session中不存在此数据时,去application中寻找数据是否存在
    5. 当application中不存在此数据时,向网页输出空字符(是"",不是null)
    6. 在上述的流程中,一旦某个步骤找到了数据,就会将数据输出到网页中,且后续流程不再执行

### taglib指令
1. 作用:用于在JSP中引入标签库,需要导入jar包
2. 语法格式:`<%@ taglib prefix="" uri=""%>`
3. 属性:
    1. prefix:是引入的标签库的名称,用于区分多个标签库.在使用此标签库中的标签时,需在标签前添加标签库名称:
    2. 例如:我们引入一个标签库,prefix=a,则其中的标签在使用时:`<a:标签名></a:标签>`
    3. uri:用于匹配标签库,在引入的tld文件中存在一个uri属性值,我们uri属性与tld文件中的属性相同时,则引入这个文件描述的标签库
    4. 

### JSTL标签库
1. 说明:是一套JSP的标准标签库,对JSP的标签进行了扩展
2. IF标签
    1. 用于判断元素是否显示
    2. 格式:`<库的名称:if test=""></库的名称:if>`
    3. test属性值:可以是boolean值,或运算结果为boolean的el表达式

3. choose+when+otherwise标签
    1. 类似Java中的:switch+case+default
    2. 这三个标签,只有when是由test属性的,属性值是boolean值,允许使用el表达式传入
    3. 作用:用于多分支显示
    4. 格式:  
```jsp
<% pageContext.setAttribute("flag",1);%>
<kuming:choose>
    <kuming:when test="${flag==1}">
        从前有座山1
    </kuming:when>
    <kuming:otherwise>
        从前有座山3
    </kuming:otherwise>
</kuming:choose>
```

4. forEach标签
    1. 作用:用于遍历集合或数组元素
    2. 格式:`<标签库名称:forEach item="" var=""></标签库名称:forEach>` 
    3. 属性:
        1. item:要遍历的数组或集合必须通过el表达式传递
        2. var:在循环遍历时,从数组或集合中取出的每一个元素会被存储到pageContext中,key就是var的值
        3. 案例:

```jsp
<kuming:forEach items="${data}" var="x">
    <h1>${x}</h1>
</kuming:forEach>
```



















