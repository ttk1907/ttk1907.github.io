---
layout: post
title:  "dubbo整合springboot基础"
date:   2020-09-01
categories: dubbo
tags: dubbo
---

* content
{:toc}

1. dubbo整合springboot基础





# dubbo整合springboot基础
## dubbo整合springboot
### 发布服务
1. 第一步：将服务注册到注册中心
    1. 首先引入dubbo和zkclient 的依赖
    2. 配置配置文件
    ```
dubbo.application.name = '模块名'
dubbo.register.address = zookeeper://服务器ip:2181
dubbo.scan.base-packages = 'service包'
    ```

2. 在service类上加@Service注解，注意：此注解要选择dubbo包下的注解(此注解学习时过时了，应为@DubboService)，和@Component
3. 发布服务

### 引用服务
1. 第一步：引入依赖
2. 第二步：配置dubbo注册中心地址
3. 第三步：引用服务
    1. 在启动类上加@EnableDubbo注解，开启dubbo
    2. 需要将使用的服务的service一模一样的抽象类
    3. 在使用的时候使用@Reference导入，这个注解是按照全类名进行引用，看那个服务向注册中心注册了此服务，就引用谁