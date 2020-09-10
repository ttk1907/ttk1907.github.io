---
layout: post
title:  "springcloud微服务架构1"
date:   2020-09-08
categories: springcloud
tags: springcloud
---

* content
{:toc}

1. 微服务架构理论入门





# 微服务架构概述
## 一、基于分布式的微服务架构，满足那些维度？支撑起这些维度的具体技术
1. 服务注册于发现
2. 服务调用
3. 服务熔断
4. 负载均衡
5. 服务降级
6. 服务消息队列
7. 配置中心管理
8. 服务网关
9. 服务监控
10. 全链路追踪
11. 自动化构建部署
12. 服务定时任务调度操作

## 二、springCloud是什么？
1. 分布式微服务架构的一站式解决方案，是多种微服务架构落地技术的集合体，俗称微服务全家桶

## 三、学习使用版本
1. cloud Hoxton.SR1
2. boot 2.2.2.RELEASE
3. cloud alibaba 2.1.0.RELEASE
4. Java java8
5. Maven 3.5以上
6. Mysql 5.7以上

## 四、各组件停更情况
1. 服务注册中心
    1. Eureka(X)
    2. Zookeeper
    3. Consul
    4. Nacos(本次重点学习)
2. 服务调用
    1. Ribbon
    2. LoadBalancer
3. 服务调用2
    1. Feign(X)
    2. OpenFeign
4. 服务降级
    1. Hystrix(快挂了，但是目前正在大规模使用)
    2. resilience4j(国外推荐，国内不常用)
    3. sentienl(推荐使用阿里的服务)
5. 服务网关
    1. Zuul(X)
    2. gateway(重点学习)
6. 服务配置
    1. Config(X)
    2. Nacos
7. 服务总线
    1. Bus(X)
    2. Nacos
8. 总结:Nacos，阿里巴巴，永远的神！
