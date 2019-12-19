---
layout: post
title:  "Java猿代码学习平台1"
date:   2019-12-16
categories: Project
tags: project
---

* content
{:toc}

1. Java猿代码学习平台1：项目需求、项目涉及技术、MAVEN应用、项目工程结构、项目数据库结构、MyBatis Generator工具使用、用户注册服务开发







# 猿代码项目流程
## 项目需求
1. www.ydma.cn
2. 在线学习系统，课程浏览、学习、学习期间可以记录笔记、评价、提问、学习朋友圈。

## 项目涉及技术
1. 前端：Ajax、js、jQuery、Vue、BootStrap、HTML5、CSS3
2. 后端：Spring、Mybatis、SpringBoot、SpringCloud、Spring Data、Spring Schedule、Spring Test、Spring Cache、Spring Task、Redis、MongoDB
3. 架构：微服务架构（分布式）、Restful服务架构、前后分离架构
4. 交互层：HTML、CSS、JS、Ajax/小程序/手机APP（tomcat集群/nginx集群）
5. 业务服务层：SSM、SpringBoot（tomcat集群）
6. 缓存层：Redis、Spring Cache (redis集群)
7. 数据存储层：MySQL、MongoDB、(MySQL、MongoDB集群)
8. 流媒体服务器：red5或七牛
9. 服务管理平台：SpringCloud

## 开发工具

IDEA、MAVEN、Tomcat 9、JDK1.8

## MAVEN应用

### MAVEN继承应用

```xml
<parent>
    <groupId>cn.xdl</groupId>
    <artifactId>xdl-parent</artifactId>
    <version>0.0.1-SNAPSHOT</version>
</parent>
```

当前project继承parent后，会将parent项目中的pom.xml定义引入到当前项目中。parent项目创建类型为pom类型。

### MAVEN聚合应用

如果有多个project，对project进行编译、打包、发布等等过程一个一个做太繁琐了，此时可以使用聚合来统一编译、打包、发布。

创建maven module项目，添加下面定义

```xml
<modules>
    <module>xdl-demo3</module>
    <module>xdl-demo4</module>
</modules>
```

提示：使用时，一般采用parent项目做聚合工程。

###MAVEN jar包依赖传递、依赖排除、依赖范围

1. 依赖传递： B包依赖A包，当C引入B包时，也会同时引入A包
2. 依赖排除：如果C引入B包时，不想引入A包，可以使用`<exclusion>`定义排除A
3. 依赖范围：jar包可以指定编译、测试、运行、发布阶段是否有效。通过`<scope>`可以指定compile、provided、runtime、test等，默认值为compile，各阶段都有效。

###项目工程结构

1. ydma-parent : 父工程、聚合工程
2. ydma-course : 课程服务模块
3. ydma-video : 视频服务模块
4. ydma-user : 用户服务模块

###项目数据库结构

![项目数据库结构](/assets/项目图片/猿代码项目/e-r.png)

###MyBatis Generator工具使用

**追加mybatis-generator-core工具包**

```xml
<dependency>
  <groupId>org.mybatis.generator</groupId>
  <artifactId>mybatis-generator-core</artifactId>
  <version>1.3.7</version>
</dependency>
```

**在src\main\resources添加mbg.xml配置文件**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE generatorConfiguration
  PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
  "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">

<generatorConfiguration>
<!-- 指定驱动包 -->
  <classPathEntry location="D:\Maven\repository\mysql\mysql-connector-java\8.0.15\mysql-connector-java-8.0.15.jar" />

  <context id="DB2Tables" targetRuntime="MyBatis3">
  
    <!-- 指定数据库连接参数 -->
    <jdbcConnection driverClass="com.mysql.cj.jdbc.Driver"
        connectionURL="jdbc:mysql://localhost:3306/ttk?useUnicode=true&amp;characterEncoding=utf8&amp;useSSL=false&amp;serverTimezone=GMT%2B8"
        userId="root"
        password="123456">
    </jdbcConnection>

    <javaTypeResolver >
      <property name="forceBigDecimals" value="false" />
    </javaTypeResolver>

  <!-- 实体类 -->
    <javaModelGenerator targetPackage="cn.xdl.ydma.entity" targetProject="src\main\java">
      <property name="enableSubPackages" value="true" />
      <property name="trimStrings" value="true" />
    </javaModelGenerator>

  <!-- SQL定义XML文件 -->
    <sqlMapGenerator targetPackage="cn.xdl.ydma.sql"  targetProject="src\main\resources">
      <property name="enableSubPackages" value="true" />
    </sqlMapGenerator>

  <!-- 与SQL映射Mapper接口,type=XMLMAPPER表示XML定义SQL语句；type="ANNOTATEDMAPPER"表示注解SQL -->
    <javaClientGenerator type="ANNOTATEDMAPPER" targetPackage="cn.xdl.ydma.dao"  targetProject="src\main\java">
      <property name="enableSubPackages" value="true" />
    </javaClientGenerator>


  <!-- 根据哪个表生成Entity、XML、Mapper -->
    <table tableName="course" domainObjectName="Course" enableCountByExample="false"
      enableDeleteByExample="false" enableSelectByExample="false" enableUpdateByExample="false">
      <generatedKey column="ID" sqlStatement="MYSQL" identity="true" />
    </table>

  </context>
</generatorConfiguration>
```

**在src\main\java定义MyBatisGenerator启动类**

```java
public class RunMyBatisGenerator {
    public static void main(String[] args) throws Exception {
        List<String> warnings = new ArrayList<String>();
        boolean overwrite = true;
        File configFile = new File("src/main/resources/mbg.xml");
        ConfigurationParser cp = new ConfigurationParser(warnings);
        Configuration config = cp.parseConfiguration(configFile);
        DefaultShellCallback callback = new DefaultShellCallback(overwrite);
        MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config, callback, warnings);
        myBatisGenerator.generate(null);
    }
}
```

##用户注册服务开发

###注册服务接口设计

1. 请求地址： http://localhost:7001/user/regist  POST
2. 请求参数：用户名name、密码password
3. 响应结果：json    {"code":xx,"msg":xx}

###注册服务接口实现

/user/regist-->UserController-->UserService-->UserMapper-->user表-->返回json结果

1. UserMapper实现
    1. 检查pom.xml是否需要引入其他jar包
    2. 检查application.properties是否需要定义参数（server,datasource）
    3. 定义启动类，追加注解标记（@SpringBootApplication、@MapperScan）
    4. 检查是否需要追加Mapper接口方法

2. UserService实现
    1. 注入UserMapper对象
    2. 调用selectByName检查用户名是否存在
    3. 调用insertSelective插入用户信息

3. UserController实现

```java
@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping("/user/regist")
    public YdmaResult regist(String name,String password) {
    return userService.addUser(name, password);
    }
}
```

4. Test测试

```java
@RunWith(SpringRunner.class)
@SpringBootTest(classes= {RunUserBoot.class})
public class TestUserController {

    @Autowired
    private UserController userController;

    @Test
    public void test1() throws Exception {
        MockMvc mock = MockMvcBuilders.standaloneSetup(userController).build();
        RequestBuilder registRequest = MockMvcRequestBuilders.post("/user/regist")
            .param("name", "scott2")
            .param("password", "1234");

        MvcResult result = mock.perform(registRequest).andReturn();
        String content = result.getResponse().getContentAsString();
        System.out.println(content);

        //将返回的json字符串转成ydmaResult对象
        ObjectMapper mapper = new ObjectMapper();
        YdmaResult ydmaResult = mapper.readValue(content, YdmaResult.class);
        //断言
        Assert.assertEquals(ydmaResult.getCode(), YdmaConstant.SUCCESS);
        Assert.assertEquals(ydmaResult.getMsg(), YdmaConstant.REGIST_SUCCESS_MSG);
    }
}
```











