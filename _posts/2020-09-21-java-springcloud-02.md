---
layout: post
title:  "springcloud微服务架构02"
date:   2020-09-21
categories: springcloud
tags: springcloud
---

* content
{:toc}

2. 单机版eureka
3. 集群版eureka
4. 修改服务主机名和ip在eureka的web上显示
5. eureka服务发现
6. Eureka自我保护


# 服务注册与发现

## Eureka:

1. 前面我们没有服务注册中心,也可以服务间调用,为什么还要服务注册?
    1. 当服务很多时,单靠代码手动管理是很麻烦的,需要一个公共组件,统一管理多服务,包括服务是否正常运行,等

2. Eureka用于**==服务注册==**,目前官网**已经停止更新**

​![](/assets/springcloud/Eureka的1.jpg)

![](/assets/springcloud/Eureka的2.jpg)

![](/assets/springcloud/Eureka的3.jpg)

![](/assets/springcloud/Eureka的4.jpg)

### 一、单机版eureka:

#### 1.创建项目cloud_eureka_server_7001

#### 2.引入pom依赖
1. eurka最新的依赖变了

![](/assets/springcloud/Eureka的5.jpg)

#### 3.配置文件:

![](/assets/springcloud/Eureka的6.jpg)

#### 4.主启动类 

![](/assets/springcloud/Eureka的7.jpg)

#### 5.此时就可以启动当前项目了

#### 6.其他服务注册到eureka:
比如此时pay模块加入eureka:

1. 主启动类上,加注解,表示当前是eureka客户端

![](/assets/springcloud/Eureka的10.jpg)

2. 修改pom,引入

![](/assets/springcloud/Eureka的8.jpg)

3. 修改配置文件:

![](/assets/springcloud/Eureka的9.jpg)

4. pay模块重启,就可以注册到eureka中了

**==order模块的注册是一样的==**

### 二、集群版eureka:

#### 1.集群原理:

![](/assets/springcloud/Eureka的11.jpg)

```java
1.就是pay模块启动时,注册自己,并且自身信息也放入eureka
2.order模块,首先也注册自己,放入信息,当要调用pay时,先从eureka拿到pay的调用地址
3.通过HttpClient调用
    并且还会缓存一份到本地,每30秒更新一次
```

![](/assets/springcloud/Eureka的12.jpg)

**集群构建原理:互相注册**

![](/assets/springcloud/Eureka的13.jpg)

#### 2.构建新erueka项目

1. 名字:cloud_eureka_server_7002
2. pom文件:粘贴7001的即可
3. 配置文件:在写配置文件前,修改一下主机的hosts文件

![](/assets/springcloud/Eureka的14.jpg)

4. 首先修改之前的7001的eureka项目,因为多个eureka需要互相注册

![](/assets/springcloud/Eureka的15.jpg)

5. 然后修改7002,**7002也是一样的,只不过端口和地址改一下**
6. 主启动类:复制7001的即可
7. 然后启动7001,7002即可

![](/assets/springcloud/Eureka的16.jpg)

#### 3.将pay,order模块注册到eureka集群中:

1. 只需要修改配置文件即可:

![](/assets/springcloud/Eureka的17.jpg)

2. 两个模块都修改上面的都一样即可,然后启动两个模块,要先启动7001,7002,然后是pay模块8001,然后是order(80)

3. 将pay模块也配置为集群模式:

#### 4.创建新模块,8002

1. 名称: cloud_pay_8002
2. pom文件,复制8001的
3. 配置文件复制8001的,端口修改一下,改为8002,服务名称不用改,用一样的
4. 主启动类,复制8001的
5. mapper,service,controller都复制一份,然后就启动服务即可,此时访问order模块,发现并没有负载均衡到两个pay,模块中,而是只访问8001,虽然我们是使用RestTemplate访问的微服务,但是也可以负载均衡的
![](/assets/springcloud/Eureka的18.jpg)

6. **注意这样还不可以,需要让RestTemplate开启负载均衡注解,还可以指定负载均衡算法,默认轮询**

![](/assets/springcloud/Eureka的19.jpg)

### 三、修改服务主机名和ip在eureka的web上显示

1. 比如修改pay模块,修改配置文件:

![](/assets/springcloud/Eureka的20.jpg)

### 四、eureka服务发现:

![](/assets/springcloud/Eureka的21.jpg)
1. 以pay模块为例,首先添加一个注解,在controller中

![](/assets/springcloud/Eureka的22.jpg)

![](/assets/springcloud/Eureka的23.jpg)

2. 在主启动类上添加一个注解

![](/assets/springcloud/Eureka的24.jpg)

**然后重启8001.访问/payment/discover**y

### 五、Eureka自我保护:

![](/assets/springcloud/Eureka的26.jpg)

![](/assets/springcloud/Eureka的27.jpg)

![](/assets/springcloud/Eureka的25.jpg)

![](/assets/springcloud/Eureka的28.jpg)

**eureka服务端配置:**

![](/assets/springcloud/Eureka的29.jpg)

![](/assets/springcloud/Eureka的30.jpg)

​**设置接受心跳时间间隔**

**客户端(比如pay模块):**

![](/assets/springcloud/Eureka的31.jpg)

**此时启动erueka和pay.此时如果直接关闭了pay,那么erueka会直接删除其注册信息**