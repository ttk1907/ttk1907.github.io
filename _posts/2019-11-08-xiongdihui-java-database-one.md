---
layout: post
title:  "Java-Jdbc第一天"
date:   2019-11-08
categories: Java
tags: Java note
---

* content
{:toc}

1. Jdbc第1天：DBC访问数据库的步骤、JDBC原理图









# Java数据存储第一天
## Java数据存储篇--Jdbc--第1天
### JDBC(Java-Database-Connectivity)
1. JDBC访问数据库的步骤、
    1. 加载驱动：用Class.forName+包名.类名就可以加载驱动`Class.forName("oracle.jdbc.OracleDriver");`
    2. 获取连接：
    ```java
//提前定义Connection,将其赋值为空
Connection conn = null;
conn = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:数据库名","账号","密码");
System.out.println(conn);
    ```

    3. 定义sql 并获取sql的执行环境 Statement 
    ```java
//提前定义执行环境
Statement st = null;
String sql="select * from emp where EMPNO = 7499";
st = conn.createStatement();
    ```

    4. 执行sql 处理sql 返回值
        1. select:返回ResultSet  遍历
        ```java
//因为是查询语句，所以必须定义一个结果集
rs = st.executeQuery(sql);
if (rs.next()){
    System.out.println(rs.getInt("EMPNO")+":"+rs.getString("ENAME"));
}
        ```
        2. dml:返回int  代表影响的数据行数
        ```java
//改一下sql语句，接受一下返回的行数
int rows = st.executeUpdate(sql);
System.out.println("rows"+rows);
        ```

    5. 释放资源:Connection、Statement、ResultSet
    ```java
//从小到大关闭
if (rs != null){
    rs.close();
} 
    ```
2. JDBC原理图
![JDBC原理图](/assets/JDBC.png)












