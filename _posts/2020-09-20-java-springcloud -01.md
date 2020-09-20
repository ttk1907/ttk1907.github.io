---
layout: post
title:  "springcloud微服务架构01"
date:   2020-09-20
categories: springcloud
tags: springcloud
---

* content
{:toc}

1. SpringCloud升级,部分组件停用
2. 环境搭建




# SpringCloud:

## 一、SpringCloud升级,部分组件停用:

1. Eureka停用,可以使用zk作为服务注册中心
2. 服务调用,Ribbon准备停更,代替为LoadBalance
3. Feign改为OpenFeign
4. Hystrix停更,改为resilence4j,或者阿里巴巴的sentienl
5. Zuul改为gateway
6. 服务配置Config改为  Nacos
7. 服务总线Bus改为Nacos

# 环境搭建:

## 1.创建父工程,pom依赖

## 2.创建子模块,pay模块
![](/assets/springcloud/sc的3.png)
### 1.子模块名字:
​   cloud_pay_8001

### 2.pom依赖

### 3.创建application.yml

```yml
server:
    port: 8001   
spring:
    application:
        name: cloud-payment-service
    datasource:
    # 当前数据源操作类型
    type: com.alibaba.druid.pool.DruidDataSource
    # mysql驱动类
    driver-class-name: com.mysql.cj.jdbc.Driver
      url: jdbc:mysql://localhost:3306/db2019?useUnicode=true&characterEncoding=
            UTF-8&useSSL=false&serverTimezone=GMT%2B8                               
    username: root
    password: root
mybatis:            
    mapper-locations: classpath*:mapper/*.xml
    type-aliases-package: com.eiletxie.springcloud.entities
            它一般对应我们的实体类所在的包，这个时候会自动取对应包中不包括包名的简单类名作为包括包名的别名。多个package之间可以用逗号或者分号等来进行分隔（value的值一定要是包的全）
```

### 4.主启动类    

### 5.业务类

#### 1.sql

![](/assets/springcloud/sc的4.png)

#### 2.实体类

![](/assets/springcloud/sc的5.png)

#### 3.entity类

![](/assets/springcloud/sc的6.png)

#### 4.dao层:

![](/assets/springcloud/sc的7.png)

#### 5.mapper配置文件类

​   **在resource下,创建mapper/PayMapper.xml**

![](/assets/springcloud/sc的8.png)

#### 6.写service和serviceImpl

![](/assets/springcloud/sc的9.png)

![sc的9](/assets/springcloud/sc的10.png)

#### 7.controller

![](/assets/springcloud/sc的11.png)

![](/assets/springcloud/sc的12.png)


## 3.热部署:

![](/assets/springcloud/sc的13.png)

![](/assets/springcloud/sc的14.png)

## 4.order模块

![](/assets/springcloud/sc的3.png)

### **1.pom**       

### **2.yml配置文件**

![](/assets/springcloud/order模块1.png)

### **3.主启动类**

### **4.复制pay模块的实体类,entity类**

### **5.写controller类**

1. 因为这里是消费者类,主要是消费,那么就没有service和dao,需要调用pay模块的方法,并且这里还没有微服务的远程调用,那么如果要调用另外一个模块,则需要使用基本的api调用
2. 使用RestTemplate调用pay模块,

​![](/assets/springcloud/order模块2.png)

![](/assets/springcloud/order模块3.png)

3. 将restTemplate注入到容器

![](/assets/springcloud/order模块4.png)

4. 编写controller:

![](/assets/springcloud/order模块5.png)



## 5.重构,

新建一个模块,将重复代码抽取到一个公共模块中

### 1.创建commons模块

### 2.抽取公共pom

![](/assets/springcloud/commons模块.png)

### 3.entity和实体类放入commons中

![](/assets/springcloud/commons模块2.png)

### 4.使用mavne,将commone模块打包(install),其他模块引入commons