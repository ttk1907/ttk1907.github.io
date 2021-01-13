---
layout: post
title:  "Java-Spring框架第六天"
date:   2019-12-02
categories: Frame
tags: Spring note
---

* content
{:toc}

1. Spring第6天:Spring AOP、AOP中涉及到概念、Spring 实现AOP的步骤、切点表达式的写法、AOP中的五种通知类型、基于标注的AOP实现、异常通知、环绕通知










# Spring第6天
## Spring AOP
### 什么是AOP
1. Aspect Oriented Programming : 面向切面编程或者面向方面编程 
2. 它是对面向对象的一个扩展 
3. 可以不修改原有代码的情况下 , 给原有的逻辑增加功能 , 降低了共通业务逻辑 和 原有逻辑的耦合度 , 因为共同业务逻辑可以通过配置手段加入到原有逻辑中

### AOP 中涉及到概念 
1. 切面 : Aspect , 封装共通业务逻辑的  
2. 连接点 : JoinPoint , 共通业务逻辑所要嵌入的位置 , 一般封装了方法的信息 
3. 切点 : Pointcut , 它是一堆连接点 , 可以看成连接点的集合(切点表达式)
4. 目标 : Target , 要嵌入共通业务逻辑的对象 
5. 代理 : Proxy , 被增强之后的目标对象 
6. 通知 : Advice , 时机
    1. 目标方法调用之前
    2. 目标方法调用之后
    3. 目标方法调用前后
    4. 目标方法最终
    5. 目标方法出现异常    
7. 最重要的三个:切面---通知---切点   

### Spring 实现AOP的步骤 
1. 建立一个项目 导入jar包(ioc aop) , 拷贝配置文件到src下 
2. 编写一个银行账户的服务类,有登录 和 注册两个方法 , 这两个方法使用伪代码即可 
3. 在配置文件中配置这个服务器类 , 然后通过容器获取服务类对应的对象 , 测试方法调用
4. 在不修改服务类代码的情况下 , 让服务类对应的方法调用前输出`******`
    1. 定义一个切面类 , 里面定义输出****** 的方法 
    2. 在配置文件中 配置切面类型的对象  
    3. 在Spring 配置文件中 写 AOP 的配置 : 切面---通知--- 切点
5. 如果配置文件里要写接口的实现类,`<bean>`里面正常写,从Spring容器里获取时要获取DAO接口类  

```xml
<bean id="accountService" class="xdl.service.AccountService"/>
<bean id="accountAspect" class="xdl.aspect.AccountAspect"/>
<aop:config>
    <aop:aspect ref="accountAspect">
        <aop:before method="dayin" pointcut="bean(accountService)"/>
    </aop:aspect>
</aop:config>
```

### 切点表达式的写法
1.  bean 限定表达式 
    1. bean(spring容器中id表达式) : 支持统配 , 如`bean(*Account)`  
2. 类型限定表达式  
    2. within(表达式): 
        1. 表达式的写法是最后一部分必须是类型 , 例如 : `com.xdl.dao.XdlBankAccountDAOOracleImp` , 对`XdlBankAccountDAOOracleImp`这个类型对应的所有方法都切入共通业务逻辑。
        2. `com.xdl.dao.*` : dao包下所有的类型  对应的方法都将被切入共通业务逻辑       
        3. `com..*` : com 包下所有的类型 以及 com的子包下所有的类型对应的方法都将被切入共通业务逻辑 
3. 方法限定表达式:
    1. execution(方法限定):
        1. 方法限定的格式 : 权限修饰 返回值类型 方法名(参数列表) throws 异常 
        2. 其中 返回值类型   方法名()  是必须的

### AOP中的五种通知类型

```xml
<aop:before   前置通知     目标方法调用之前调用 >
<aop:after    最终通知     目标方法调用后 一定会调用 >
<aop:after-returning   后置通知    目标方法调用之后调用 >   
<aop:after-throwing    异常通知    目标方法调用出现异常 采用调用 >
<aop:around    环绕通知      目标方法调用前后都调用  >
```

### 基于标注的AOP实现
1. 写一个DAO 接口 , 并开发一个DAO接口的实现类然后使用组件扫描在容器中创建DAO实现类的组件 , DAO 和 接口使用伪代码即可。
    1. 建立项目  导入jar包(ioc aop) 拷贝配置文件到src
    2. 开启组件扫描
    3. 编写DAO 接口 
    4. 编写实现类    
    5. 在类上打对应的标注 测试 
2. 在上面的基础上使用标注形式的AOP给方法增加功能 
    1. 编写一个切面类  定义切面方法 打印######
    2. 开启标注形式的 aop : `<aop:aspectj-autoproxy   proxy-target-class="true" />`
    3. 创建切面组件 `@Component` 然后普通切面类变成真正的切面
    4. @Aspect 在切面方法上 , 对应通知对应的标注并在标注中写切点表达式即可

    ```java
@Component
@Aspect
public class AspectClass {
    @After("bean(account*)")
    public void dayin(){
        System.out.println("######");
    }
}
    ```   

3. AOP 中五种通知对应的标注 
    1. 前置通知 : @Before
    2. 后置通知 : @AfterReturning 
    3. 最终通知 : @After
    4. 异常通知 : @AfterThrowing
    5. 环绕通知 : @Around

### 异常通知
1. 什么时间,什么方法,出了什么异常

```java
@AfterThrowing(pointcut = "within(xdl..*)",throwing = "e")
public void runTimeException(JoinPoint jp , Exception e){
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat();
    String strTime = sdf.format(date);
    System.out.println(strTime+"||"+jp.getSignature()+"||"+e);
}
```

### 环绕通知
1. 统计每个方法的执行时间

```java
@Around("within(xdl..*)")
public Object methodTimes(ProceedingJoinPoint pjp) throws Throwable{
    long startTime = System.currentTimeMillis();
    Object obj = pjp.proceed();
    long endTime = System.currentTimeMillis();
    System.out.println(pjp.getSignature()+":用了"+(endTime-startTime)+"毫秒");
    return obj;
}
```












