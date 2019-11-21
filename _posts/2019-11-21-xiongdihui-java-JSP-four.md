---
layout: post
title:  "Java-JSP第四天"
date:   2019-11-21
categories: Java
tags: Java note
---

* content
{:toc}

1. JSP第4天：过滤器、过滤器链、Listener








# Java-JSP第四天
## Java--JSP--第4天
### JavaWeb三大组件
1. Servlet 处理请求
2. Fileter 过滤器
3. Listener 监听器

### 过滤器
1. 过滤的是请求,面向切面编程的思想
2. 使用步骤
    1. 编写一个类,实现Filter接口,重写doFilter方法
    2. 通过web.xml或注解的方式,配置过滤器的过滤地址
    3. 放行代码:`fc.doFilter(request,response);`
3. doFilter中的请求与响应对象为什么不是http的?
    1. 过滤器早期设计时,不只是针对http请求,针对所有协议的请求都可以进行过滤,因为我们现在使用的都是http协议,所以感觉很怪异,想要操作HTTP相关的请求对象与响应对象怎么办?只需要将请求对象强制转换为HttpServletRequest将响应对象强制转换为HttpServletResponse即可
4. 登录流程  
![登录流程图](/assets/登录流程图.png)

```java
@Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletRequest;
        //1.先得到session
        HttpSession session = request.getSession();
        //2.判断等没登录
        if (session.getAttribute("username")!=null){
            //放行
            filterChain.doFilter(request,response);
        }else{
            //没登陆过,重定向到登录错误页面
            response.sendRedirect("loginError.jsp");
        }
    }
```

### 过滤器链
1. 当多个过滤器的过滤地址重复时,就形成了过滤器链,用户的一次请求,需要经过多次过滤放行
2. 过滤链的执行顺序是:
    1. web.xml中配置的顺序:按照xml中配置的先后顺序来执行的,web.xml中配置代码靠前的,优先执行.
    2. 注解配置的顺序:
        1. 按照类名的自然顺序,排序执行;
        2. 注意:注解配置的过滤器,一定执行在web.xml过滤器之后
        3. 例如:类名Filter1执行在类名Filter2之前.
        4. 例如:类名Aaa执行在类名Aab之前

### Listener
1. 事件驱动,监听的是tomcat产生的事件
2. 两类事件:
    1. 生命周期相关事件
    2. 域对象中数据的变化事件
3. ServletContextListener
    1. 用于监听ServletContext的创建和销毁
    2. 因为ServletContext的创建就表示项目的启动.ServletContext的销毁就表示项目的关闭,所以此监听器是用于监听项目的启动和关闭的
    3. 我们常在项目启动时,进行资源初始化的操作.准备一些后续项目中会用到的资源.在项目关闭时,进行资源的释放操作.解除资源的占用句柄






















 
















