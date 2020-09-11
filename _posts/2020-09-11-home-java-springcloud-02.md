---
layout: post
title:  "springcloud微服务架构2"
date:   2020-09-11
categories: springcloud
tags: springcloud
---

* content
{:toc}

1. 环境搭建
2. 导入父工程的依赖
3. **dependencyManagement**和**dependencies**区别
4. 跳过maven的单元测试 





# 环境搭建
## 一、springcloud整体聚合父工程
1. New Project
2. 聚合总父工程名字
3. Maven选版本
4. 工程名字
5. 字符编码 editor -> file encodings
6. 注解生效激活 build -> compiler -> annotation processors
7. java编译版本选8
8. File Type过滤

## 二、导入父工程的依赖

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ttk.springcloud</groupId>
    <artifactId>cloud2020</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <!--  统一jar包和版本号的管理-->
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
        <junit.version>4.12</junit.version>
        <log4j.version>1.2.17</log4j.version>
        <lombok.version>1.16.18</lombok.version>
        <mysql.version>5.1.47</mysql.version>
        <druid.version>1.1.16</druid.version>
        <mybatis.spring.boot.version>1.3.0</mybatis.spring.boot.version>
    </properties>
    <!--  子模块继承之后,提供作用:锁定版本+子module不用写groupId和version-->
    <dependencyManagement>
        <dependencies>
            <!--      spring boot 2.2.2-->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.2.2.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!--      spring cloud Hoxton.SR1-->
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Hoxton.SR1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <!--      spring cloud alibaba 2.1.0.RELEASE-->
            <dependency>
                <groupId>com.alibaba.cloud</groupId>
                <artifactId>spring-cloud-alibaba-dependencies</artifactId>
                <version>2.1.0.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>${mysql.version}</version>
            </dependency>
            <dependency>
                <groupId>com.alibaba</groupId>
                <artifactId>druid</artifactId>
                <version>${druid.version}</version>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>${mybatis.spring.boot.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
  
</project>
```

## 三、知识点复习
1. **dependencyManagement**和**dependencies**区别
    1. **dependencyManagement**用于父类管理的,一般是最顶层的父pom才会看到这个,作用是能让所有在子项目中引用一个依赖而不用显式的列出版本号,Maven会沿着父子层次向上走,直到找到一个拥有**dependencyManagement**元素的项目,然后它就会使用这个**dependencyManagement**元素中指定的版本号
    2. 这样做的好处是:如果有多个子项目都引用同一样依赖,则可以避免在每个使用的子项目里都声明一个版本号,这样当想升级或切换到另一个版本时,只需要在顶层父容器里更新,而不需要一个一个子项目的修改;如果某个子项目需要另外一个版本,只需要声明**version**即可
    3. 注意:**dependencyManagement**里只是声明依赖,<font color=red face="黑体">并不实现引入</font>,因此子项目需要显示的声明需要使用的依赖
    4. 如果不在子项目中声明依赖,是不会从父项目中继承下来的;只有在子项目中写了该依赖项,并且没有指定具体版本,才会从父项目中继承该项目,并且**version**和**scope**都读取自父pom
    5. 如果子项目指定了版本号,那么会使用子项目中指定的jar版本
2. 如何跳过maven的单元测试
    1. idea右侧maven上边的小闪电图标,点下去过生命周期中的test就被跳过去了