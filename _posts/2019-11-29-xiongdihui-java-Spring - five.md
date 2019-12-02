---
layout: post
title:  "Java-Spring框架第五天"
date:   2019-11-29
categories: Spring
tags: Spring note
---

* content
{:toc}

1. Spring第5天:Spring 的异常处理、文件上传、Spring MVC的控制器方法 如何返回 JSON、rest、使用rest完成增加、使用rest完成更新










# Spring第5天
## Spring 的异常处理 
1. 配置一个系统提供的异常处理器 , 出现什么异常就跳转到对应的页面

```xml
<!--  配置系统提供的异常处理器  -->
<bean  id="exceptionResolver"  
    class="org.springframework.web.servlet.handler.SimpleMappingExceptionResolver">
    <property name="exceptionMappings">
        <props>
            <prop key="java.lang.Exception">error2</prop> 
            <prop key="java.lang.RuntimeException">error</prop> 
        </props>
    </property>
</bean>
``` 

2. 全局处理 ---- 自定义异常处理器 
    1. 实现HandlerExceptionResolver , 让对应的异常跳转到对应的页面 

```java
@Override
    public ModelAndView resolveException(HttpServletRequest arg0, HttpServletResponse arg1, Object arg2,Exception e) {
        ModelAndView  mav  = new ModelAndView();
    // 出现什么样的异常  就跳转到对应的页面 
    if(e instanceof RuntimeException) {
      mav.setViewName("error");
    }else if(e instanceof Exception) {
      mav.setViewName("error2");
    }
    return mav;
} 
```

3. 局部异常处理 ---- 只针对一个具体的控制器起作用,(异常方法中Exception的参数必须有)

```java
@ExceptionHandler
public  String  foo(Exception  e) {
    System.out.println(e.getMessage());
    return  "error3";
}   
```

## 文件上传  
1. 写一个文件上传的页面
    1. 注意三点  
        1. 第一必须以post 提交    
        2. enctype="multipart/form-data"
        3. type="file" 
2. 编写一个文件上传的控制器 , 接收文件数据 和 非文件数据 
3. 这个控制器需要依赖于文件解析器 , 文件解析器依赖于文件上传的jar

## Spring MVC的控制器方法 如何返回 JSON
1. 搭建一个基于标注的MVC
2. 在控制器中编写一个控制器方法   

```java
  @RequestMapping("/请求的路径")
  public  要转换成JSON的数据类型    方法名任意(参数任意){
  
  }
```

3. 为了处理返回的数据为JSON , 需要加一个@ResponseBody(把数据转换成JSON 同时告知mvc 返回值不要经过视图处理器) , 这个标注要依赖于 JSON的转换包  

## rest
1. 什么rest  
    1. REST即表述性状态传递（英文：Representational State Transfer，简称REST）
    2. 是Roy Fielding博士在2000年他的博士论文中提出来的一种软件架构风格。
    3. 这个软件架构基于http 协议 , 它可以提高系统的可伸缩性 , 降低应用之间的耦合度 , 便于分布式应用程序的开发。
2. rest 的两个核心规范 
    1. 定位资源的URL做了限定 , 把原来基于操作的设计改成了基于资源的设计 
    2. 对资源的操作的做了限定 , Http协议的请求方式上 , Get用来查询 , Post增加 , Put更新 , Delete删除 
3. 什么是restful?
    1. 符合rest 风格和约束的应用程序 叫restful
4. Spring MVC对rest 的支持
    1. 搭建一个基于标注的 MVC
    2. 在控制器方法上 , 支持对应的请求方式 : `@RequestMapping(value="/account/{变量名}",method=RequestMethod.GET)`
    3. 获取路径变量上的值 : `@PathVariable("路径变量名")` , 加在控制器参数上 
    4. rest 请求的路径是没有后缀的 , 所以需要把DispatcherServlet 中的 url-parttern  改成  支持所有请求的`/`
    5. 如果 改成 `/` 则所有的静态资源被拦截 , 需要在application.xml中配置`<mvc:default-servlet-handler/>`

## 使用rest 完成增加 
1. js部分

```js
<script type="text/javascript">
    function  addAccount(){
        var  id = $("#id").val();
        var  acc_no = $("#acc_no").val();
        var  acc_password = $("#acc_password").val();
        $.ajax({
            url:"account/"+id,
            type:"post",
            success:function(res){
                alert(res);
            },
            data:{id:id,acc_no:acc_no,acc_password:acc_password,
                acc_money:10000+parseInt(id)},
            dataType:"json"
        });
    }
</script>
```

2. 控制器部分

```java
@RequestMapping(value="/account/{id}",method=RequestMethod.POST)
@ResponseBody
public  boolean   accountRemoveById(XdlBankAccount  account) {
    System.out.println(account);
    return  true;
}   
```

## 使用rest 完成更新 
1. 在完成增加的基础上完成更新 
2. 前端ajax的处理 
    1. 把post 改成  put
    2. contentType:"application/json" , 要求参数必须以json字符串进行传递 
    3. JSON.stringify : 可以把JSON对象转换成 JSON字符串 
3. 控制器上的处理
    1. 把POST 改成 PUT
    2. 把JSON字符串 , 变成JAVA对象 : @RequestBody  
  
4. js部分

```js
<script type="text/javascript">
    function  updateAccount(){
        var  id = $("#id").val();
        var  acc_no = $("#acc_no").val();
        var  acc_password = $("#acc_password").val();
        $.ajax({
            url:"account/"+id,
            type:"put",
            success:function(res){
                alert(res);
            },
            contentType:"application/json",  
            data:JSON.stringify({id:id,acc_no:acc_no,acc_password:acc_password,
                acc_money:10000+parseInt(id)}),
            dataType:"json"
        });
    }
</script>
```

5. 控制器部分

```java
@RequestMapping(value="/account/{id}",method=RequestMethod.PUT)
@ResponseBody
public  boolean   accountUpdate(@RequestBody XdlBankAccount  account) {
    System.out.println(account);
    return  true;
} 
```











































