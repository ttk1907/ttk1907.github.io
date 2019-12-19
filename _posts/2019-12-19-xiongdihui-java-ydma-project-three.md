---
layout: post
title:  "Java猿代码学习平台3"
date:   2019-12-19
categories: Project
tags: project
---

* content
{:toc}

1. Java猿代码学习平台3：工作总结、MyBatis多表操作、用户登录服务、用户身份认证、、、、







####工作总结

登录注册服务：/user/regist   POST

用户登录服务：/user/login  POST

根据ID查询课程服务：/course/xx GET

根据学科分页查询课程服务：/course/list  GET

SSM，基于SpringBoot的SSM使用，SpringBoot对Spring应用封装和简化。开发Restful服务。



##MyBatis多表操作

MyBatis关联查询，多表从查询数据。将多个表查询的记录映射成具有关联关系的对象。

```java
DEPT-->Dept
EMP(deptno)-->Emp
public class Dept{
    private int id;
    private String dname;
    private String loc;
    private List<Emp> emps;
}
```

###基于关联查询加载章节相关的视频记录

1. 在章节对象类型中添加关联属性

```java
public class Chapter{
  //因为有多条记录关联，所以选择List集合
  private List<Video> videos;
}
```

2. 在章节查询语句映射中定义videos加载过程@Many

```java
@Select({
"select",
"id, name, course_id",
"from chapter",
"where course_id = #{id,jdbcType=INTEGER}"
})
@Results({
    @Result(column="id", property="id", jdbcType=JdbcType.INTEGER, id=true),
    @Result(column="name", property="name", jdbcType=JdbcType.VARCHAR),
    @Result(column="course_id", property="courseId", jdbcType=JdbcType.INTEGER),
    @Result(property="videos",column="id"
        ,many=@Many(select="cn.xdl.ydma.dao.VideoMapper.selectByChapterId"))
})
List<Chapter> selectByChapterId(Integer id);
```

3. 在VideoMapper中定义selectByChapterId方法

```java
@Select({
    "select",
    "id, name, url, chapter_id",
    "from video",
    "where chapter_id = #{id,jdbcType=INTEGER}"
  })
@Results({
    @Result(column="id", property="id", jdbcType=JdbcType.INTEGER, id=true),
    @Result(column="name", property="name", jdbcType=JdbcType.VARCHAR),
    @Result(column="url", property="url", jdbcType=JdbcType.VARCHAR),
    @Result(column="chapter_id", property="chapterId", jdbcType=JdbcType.INTEGER)
})
List<Video> selectByChapterId(Integer id);
```

###根据课程ID查询章节及视频列表

  请求地址: /course/chapter/video
  请求参数：课程ID cid
  响应结果：{"code":xx,"msg":xx,"data":xx}

##用户登录服务

/user/login（post）  --> UserController --> UserService -->UserMapper-->DB(user) -->返回统一json结果


##用户身份认证

常用身份认证模式：

1. 通过账号和密码，登录成功后用Session保持用户状态信息（集群情况下需要考虑Session同步，可以借助于redis）
2. 基于token令牌模式（账号和密码正确后，服务器颁发令牌给客户保存，客户请求携带token令牌，适用于分布式系统）
    - 自定义令牌规则
    - 利用JWT标准创建令牌（本系统选用）
    - 使用oauth2框架（第三方登录认证）       

3. 基于证书认证模式，（证书文件存储，例如银行、财务等系统）

4. JWT标准：JSON Web Token，是一个开放标准(RFC 7519),它定义了一种紧凑的、自包含的方式,用于作为JSON对象在各方之间安全地传输信息。

5. JWT结构由三部分构成，jwt头、有效载荷、签名  

    1. jwt头，指定签名部分采用的加密算法，令牌类型，一般都为  
        {  
            alg : HS256,  
            typ : jwt  
        }

    2. 有效载荷，可以存放用户信息，有约定属性，也可以自定义属性。
        1. exp：到期时间
        2. sub：主题 
        3. iss：发行人 
        4. iat：发布时间 
        5. aud：用户

    3. 签名，使用一个签名密码，采用SHA256(base64(头)+base64(有效载荷),"签名密码") 格式处理。


JWT格式token如下：
`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySWQiOjEyMywiVXNlck5hbWUiOiJhZG1pbiJ9.Qjw1epD5P6p4Yy2yju3-fkq28PddznqRj3ESfALQy_U`

6. Java使用JWT token认证模式
使用java-jwt工具包，创建和验证token令牌信息。

```xml
<dependencies>
    <dependency>
        <groupId>com.auth0</groupId>
        <artifactId>java-jwt</artifactId>
        <version>3.8.0</version>
    </dependency>
</dependencies>
```

7. 基于java-jwt包编写JWtUtil工具类

```java
  public class JWTUtil {
    
    private static final long EXPIRE_TIME = 15 * 60 * 1000;
    private static final String TOKEN_SECRET = "dsdsa221";
    
    /**
     * 生成签名，15分钟过期
     * @param **username**
    * @param **password**
    * @return
     */
    public static String sign(User user) {
        try {
            // 设置过期时间
            Date date = new Date(System.currentTimeMillis() + EXPIRE_TIME);
            // 私钥和加密算法
            Algorithm algorithm = Algorithm.HMAC256(TOKEN_SECRET);
            // 设置头部信息
            Map<String, Object> header = new HashMap<>(2);
            header.put("typ", "JWT");
            header.put("alg", "HS256");
            // 返回token字符串
            return JWT.create()
                    .withHeader(header)
                    .withClaim("aud", user.getName())
                    .withClaim("uid", user.getId())
                    .withExpiresAt(date)
                    .sign(algorithm);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    
    /**
       *      检验token是否正确
     * @param **token**
     * @return
     */
    public static boolean verify(String token){
        try {
            Algorithm algorithm = Algorithm.HMAC256(TOKEN_SECRET);
            JWTVerifier verifier = JWT.require(algorithm).build();
            verifier.verify(token);
            return true;
        } catch (Exception e){
            return false;
        }
    }
    
    /**
       *      从token解析出uid信息
     * @param token
     * @param key
     * @return
     */
    public static int parseTokenUid(String token) {
      DecodedJWT jwt = JWT.decode(token);
      return jwt.getClaim("uid").asInt();
    }
  }
```










