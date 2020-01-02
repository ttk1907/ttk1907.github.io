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

0. 其他
    1. `list.size()==0` 或 `list.isEmpty()` 判断列表是否为空

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
    6. jquery模拟事件 : 点击SubmitExcelFile触发filepath的点击事件

    ```js
$("#SubmitExcelFile").click(function () {
    $("#filepath").trigger("click");
})
    ```
                    

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


6. Thymeleaf模板引擎
    1. 页面上用时间戳转换时间格式必须用long类型:`${#dates.format(teacherLog.add_time*1000, 'yyyy-MM-dd HH:mm:ss')}`

7. cookie
    1. 放cookie
    ```java
//登录时添加cookie,测试用
Cookie name = new Cookie("name", teacher_name);
Cookie teacherId = new Cookie("teacherId", teacher_id+"");
Cookie teacherIp = new Cookie("teacherIp", add_ip);
//设置cookie存在时间
name.setMaxAge(60 * 60 * 24);
teacherId.setMaxAge(60 * 60 * 24);
teacherIp.setMaxAge(60 * 60 * 24);
//设置cookie存在路径
name.setPath("/");
teacherId.setPath("/");
teacherIp.setPath("/");
//发送cookie
response.addCookie(name);
response.addCookie(teacherId);
response.addCookie(teacherIp);
    ```

    2. 取cookie
    ```java
//将老师操作放到日志中
Cookie[] cookies = request.getCookies();
//获得日志中需要的数据
String teacherId = "teacherId";
String name = "name";
String action = "添加学生"+student.getUsername();
long add_time = SomeMethods.getCurrentTime();
String teacherIp = "teacherIp";
//将日志数据添加到日志实体类中
teacherLog.setAction(action);
teacherLog.setAdd_time(add_time);
for(Cookie cookie:cookies){
    if (cookie.getName().equals(name)){
        teacherLog.setTeacher_name(cookie.getValue());
    }
    if (cookie.getName().equals(teacherId)){
        //将字符串形式的id转换成int类型
        int teacher_id = Integer.parseInt(cookie.getValue());
        teacherLog.setTeacher_id(teacher_id);
    }
    if (cookie.getName().equals(teacherIp)){
        teacherLog.setAdd_ip(cookie.getValue());
    }
}
    ```

