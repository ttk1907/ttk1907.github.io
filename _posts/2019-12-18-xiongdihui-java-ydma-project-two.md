---
layout: post
title:  "Java猿代码学习平台2"
date:   2019-12-18
categories: Project
tags: project
---

* content
{:toc}

1. Java猿代码学习平台2：用户登录服务实现、课程查询服务、按学科推荐课程服务、Json Web Token（JWT）







## 用户登录服务实现

### 登录服务接口设计

  请求地址: /user/login   POST
  请求参数: 用户名name，密码password
  响应结果: {"code":xx,"msg":xx,"data":xx}

### 登录服务实现流程

  /user/login-->UserController-->UserService-->UserMapper-->user表查询检查-->返回json结果

1. 实现UserMapper
2. 实现UserService
3. 实现UserController
4. Junit+SpringTest测试

jackson序列化时将某些属性排除

- 类前使用@JsonIgnoreProperties(value= {"password","salt"})
- 方法前使用@JsonIgnore

jackson序列化时将某些null值排除

- 使用@JsonInclude(value=Include.NON_NULL) 

    Include.Include.ALWAYS 默认 
    Include.NON_DEFAULT 属性为默认值不序列化 
    Include.NON_EMPTY 属性为 空（“”） 或者为 NULL 都不序列化 
    Include.NON_NULL 属性为NULL 不序列化 



## 课程查询服务

### 课程查询服务接口设计

  请求地址：/course/xx    GET
  请求参数：无
  响应结果：{"code":xx,"msg":xx,"data":xx}

### 课程查询服务实现

  /course/xx-->CourseController-->CourseService-->CourseMapper-->course表查询-->返回JSON结果

1. 实现CourseMapper
2. 实现CourseService
3. 实现CourseController


创建ydma-common工程，与ydma-parent关系是聚合，取消继承关系，ydma-parent引用ydma-common，用于定义重用的组件。

## 按学科推荐课程服务

### 服务接口设计

  请求地址： /course/subject
  请求参数：学科ID sid 必须, 显示页数 page 可选，默认1，推荐数量 size 可选，默认4
  响应结果：{"code":xx,"msg":xx,"data":xx}

### 服务实现

  /course/subject-->CourseController-->CourseService-->CourseMapper-->course查询-->返回JSON结果

1. CourseMapper

  根据学科ID查询课程

2. CourseService

  获取前size个，分页操作取第一页

3. CourseController

  接收/course/subject请求及sid和size参数，返回json结果

## Json Web Token（JWT）

本系统采用SSO(Single sign On)单点登录结构，从认证系统登录(ydma-user)，用户和密码验证成功颁发一个token，之后携带token可以访问其他系统功能。

基于JWT标准生成Token以及token验证。











