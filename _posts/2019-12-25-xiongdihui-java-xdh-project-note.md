---
layout: post
title:  "兄弟会后台管理系统笔记"
date:   2019-12-25
categories: Project
tags: project note
---

* content
{:toc}

1. 兄弟会后台管理系统笔记






## 兄弟会后台管理系统笔记

1. 写xml中的sql语句时,传入多个参数可以使用JavaBean,直接在控制器上写接受参数的Bean对象就行

```xml
<insert id="insertData" keyProperty="Bean">
    insert into Products (ProductID, ProductName, Price, ProductDescription)
    values (#{ProductID},#{ProductName},#{Price},#{ProductDescription})
</insert>
```

2. jquery
    1. 清空输入框的值,是选中元素后用`.val("")`
    2. 刷新页面 : window.location.reload();
    3. 更改标签属性 : $("#search").attr("href","/student/like/"+searchContent);
    4. 判断空值和空格 : $("#searchContent").val().trim()==""
    5. 重定向 : window.location.href="/student/graduate/0";
                    

3. Ajax

```js
<script>
    $("#submit").click(function () {
        var name = $("#username").val();
        var sex = $("#sex").val();
        var mobile = $("#mobile").val();
        $.post("/student/add",
            {
                username:name,
                sex:sex,
                mobile:mobile
            },
            function (data) {
                alert(data.msg);
                $("#username").val("");
                $("#mobile").val("");
            });
    });
</script>
```

4. 验证手机号

```java
public static boolean isMobile(final String str) {
      Pattern p = null;
      Matcher m = null;
      boolean b = false;
      p = Pattern.compile("^[1][3,4,5,7,8][0-9]{9}$"); // 验证手机号
      m = p.matcher(str);
      b = m.matches();
      return b;
```

5. 验证输入框发送的参数不为空,空字符串和空格等

```java
student.getUsername().trim().isEmpty()
```






