---
layout: post
title:  "Java-Spring框架第四天"
date:   2019-11-28
categories: Frame
tags: Spring note
---

* content
{:toc}

1. Spring第4天:如何把控制器的数据传递给页面、中文参数乱码问题、拦截器










# Spring第4天
## 如何把控制器的数据传递给页面
1. 使用域对象传递数据 : request、session、ServletContext
2. 使用ModelAndView 传递数据 
    1. mav.getModel().put("acc_no", acc_no);
    2. mav.getModelMap().put(key, value)
    3. mav.getModelMap().addAttribute("acc_no", acc_no);  
3. 使用Model 传递数据 : addAttribute("key",value)
4. 使用ModelMap 传递数据 : addAttribute("key",value)
  或者 put("key",value)
5. 使用自定义类型的控制器参数 直接进行传递,取值时类名首字母小写 **或者** @ModelAttribute("account")  可以改变默认传递的名字 

## Spring MVC 中如何实现转发与重定向 
1. 当控制器方法返回String 时,使用redirect:+请求方法完成重定向:`return  "redirect:toLogin.do";`
2. 当控制器方法返回String 时,使用forward:+请求方法完成转发:`return  "forward:toLogin.do";`    
3. 当控制器方法返回ModelAndView时,RedirectView  重定向的view      

```java
public  ModelAndView   register7(
    @ModelAttribute("account") XdlBankAccount  account,ModelAndView  mav) { 
    RedirectView  rv  = new RedirectView("toLogin.do");
    mav.setView(rv);
    return  mav;
}
```

## 中文参数乱码问题 
1. tomcat8   get 方式没有乱码
2. 之前的解决方案依然可用 , 但必须完全遵守之前的方式 :`request.setCharacterEncoding("utf-8")`
3. 编码过滤器

```xml
<!--  配置一个编码过滤器  -->
<filter>
   <filter-name>CharacterEncoding</filter-name>
   <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
   <init-param>
       <param-name>encoding</param-name>
       <param-value>utf-8</param-value>
   </init-param>
</filter>
<filter-mapping>
   <filter-name>CharacterEncoding</filter-name>
   <url-pattern>*.do</url-pattern>
</filter-mapping>
```

## 拦截器
1. 拦截器接口的三个方法:HandlerInterceptor  
    1. preHandle : 在HandlerMapping之后 , Controller之前调用,这个方法返回 false代表终止后续调用,如果返回true代表继续后续调用。
    2. postHandle : 控制器之后 , 视图处理器之前
    3. afterCompletion : 视图处理器之后 , 响应之前 
2. 拦截器的使用步骤 
    1. 搭建一个基于标注的 spring MVC(让用户发起登录,如果账号不是 abc 密码是123 则登录成功,登录成功就把账号放入session中,重定向到 main.jsp。如果登录失败则提示用户登录失败。)
    2. 写一个拦截器 , 实现HandlerInterceptor 接口    
    3. 在Spring 配置文件中 , 配置拦截器 

```xml
<!--  配置拦截器  -->
<mvc:interceptors>
     <mvc:interceptor>
          //拦截的路径  比如 /*  拦截所有的一级请求   /** 拦截所有请求
          <mvc:mapping path=""/>
          //不拦截的请求 , 可以有多个
          <mvc:exclude-mapping path=""/>
          //拦截器对象
          <bean class="xdl.interceptor.LoginInterceptor"/>
     </mvc:interceptor>
</mvc:interceptors>
```



















