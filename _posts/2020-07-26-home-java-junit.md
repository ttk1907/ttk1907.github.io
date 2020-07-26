---
layout: post
title:  "SpringBoot测试单元"
date:   2020-07-26
categories: Project
tags: junit
---

* content
{:toc}

1. SpringBoot测试单元





## SpringBoot测试单元

### 准备

1. 使用SpringBoot自带的单元测试首先需要添加test依赖

```java
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

2. 然后在每个创建出来的测试类上加对应的标注
```java
@RunWith(SpringRunner.class)
@SpringBootTest
```

3. 注意:创建出的测试类应该以被测试的类+Test命名,然后应该与启动类放在同一级目录下,测试方法上需要加上`@Test`,然后即可正常测试







