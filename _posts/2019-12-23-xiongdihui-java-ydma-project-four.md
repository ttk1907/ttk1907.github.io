---
layout: post
title:  "Java猿代码学习平台4"
date:   2019-12-19
categories: Project
tags: project
---

* content
{:toc}

1. Java猿代码学习平台4：SpringBoot访问Redis操作、、、、、






##SpringBoot访问Redis操作

在spring-data-redis工具有一个RedisTemplate对象，可以使用该对象对redis操作。

对jedis的API进行了封装，对象序列化和反序列化进行了封装。

1. 在原始Spring框架中配置RedisTemplate

```xml
<bean id="redisFactory" class="org.springframework.data.redis.connection.jedis.JedisConnectionFactory">
    <property name="hostName" value="192.168.95.128"></property>
    <property name="port" value="6379"></property>
</bean>

<bean id="redisTemplate" class="org.springframework.data.redis.core.RedisTemplate">
    <property name="connectionFactory" ref="redisFactory"></property>
    <property name="keySerializer">
        <bean class="org.springframework.data.redis.serializer.StringRedisSerializer"/>
    </property>
</bean>
```

2. 在SpringBoot框架中使用方法

- 在pom.xml引入spring-boot-starter-data-redis启动器
- 在application.properties定义redis访问参数
- 通过自动配置会创建RedisTemplate对象，直接注入使用

```java
@Autowired
private RedisTemplate<Object, Object> redisTemplate;

@Override
public YdmaResult loadCourse(int id) {
YdmaResult result = new YdmaResult();
//先查询Redis缓存
Course course = (Course)redisTemplate.opsForValue().get("course:"+id);
if(course == null) {
    //缓存没有，再调用dao查询DB
    course = courseDao.selectByPrimaryKey(id);
    //将查询的course放入Redis缓存
    redisTemplate.opsForValue().set("course:"+id, course);
    System.out.println("从DB查询");
}

if(course != null) {
    result.setCode(YdmaConstant.SUCCESS);
    result.setMsg(YdmaConstant.LOAD_SUCCESS_MSG);
    result.setData(course);
}else {
    result.setCode(YdmaConstant.ERROR1);
    result.setMsg(YdmaConstant.LOAD_ERROR1_MSG);
}
    return result;
}
```









