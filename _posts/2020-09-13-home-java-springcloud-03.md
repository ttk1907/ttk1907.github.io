---
layout: post
title:  "springcloud微服务架构3"
date:   2020-09-13
categories: springcloud
tags: springcloud
---

* content
{:toc}

1. 微服务模块构建





# 微服务模块构建
## 一、大体流程
1. 建module
2. 改pom
3. 写yml
4. 主启动
5. 业务类

## 二、热部署
1. 添加热部署依赖
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
```

2. 热部署工具
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <fork>true</fork>
                <addResources>true</addResources>
            </configuration>
        </plugin>
    </plugins>
</build>
```

## 三、RestTemplate
1. 使用
    1. 使用restTemplate访问restful接口非常简单粗暴无脑。(url,requestMap,ResponseBean.class)这三个参数分别代表Rest请求地址、请求参数、HTTP响应转换被转换成的对象类型
2. ApplicationContextConfig

```java
@Configuration
public class ApplicationContextConfig {
    @Bean
    public RestTemplate getRestTemplate(){
        return new RestTemplate();
    }
}
```

## 四、工程重构
1. 创建cloud-api-commons模块,install到本地仓库供其他模块使用
2. 在别的模块引入对应的依赖即可实现复用


