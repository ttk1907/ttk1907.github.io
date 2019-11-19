---
layout: post
title:  "Java-Jdbc第二天"
date:   2019-11-11
categories: Java
tags: Java note
---

* content
{:toc}

1. Jdbc第2天：使用PreparedStatement 替换 Statement、工具类、配置文件、DAO
2. Jdbc第3天：JDBC事务的概念、JDBC事务操作格式、批处理、连接池、DBCPUtil工具类、数据库优化









# Java-Jdbc第二天
## Java数据存储篇--Jdbc--第2天
### 使用PreparedStatement 替换 Statement  
1. PreparedStatement相对于Statement的优点  
    1. 可以防止拼接的sql注入原理就是你输入的数据不拼接直接作为真实数据
    2. 由于采用预编译会提前生成sql的执行计划提高执行效率
    3. 拼接sql每次sql是不同的，这会给数据库服务器的sql缓冲造成冲击，无法实现批处理 
    4. 由于不拼接sql，程序员出错的概率会降低，提高编码质量和速度
2. PreparedStatement常用方法
    1. boolean execute();执行此PreparedStatement对象中的SQL语句，这可能是任何类型的SQL语句
    2. ResultSet executeQuery();执行此PreparedStatement对象中的SQL查询，并返回查询PreparedStatement的ResultSet对象
    3. int executeUpdate();执行在该SQL语句PreparedStatement对象，它必须是一个SQL数据操纵语言(DML)语句，如INSERT， UPDATE或DELETE;或不返回任何内容的SQL语句，例如DDL语句。 
3. 语法格式    
```java
PreparedStatement ps = null;
String sql = "select * from myemp where ename = ? and deptno = ?";
ps = conn.prepareStatement(sql);
//给sql语句中的？占位符传参数从1开始而不是从开始
ps.setString(1,"员工姓名");
ps.setInt(2,"部门编号");
rs1 = ps.executeQuery();
```

### 工具类
1. 工具类的思想
    1. 负责获取数据库的连接
    2. 以及资源的释放
    3. 提高代码的复用性

### 配置文件
1. 配置文件的思想
    1. 可以不修改源代码的情况下
    2. 修改参数数据 
```java
/*封装工具类，实现接连数据库的功能*/
private static String driverClassName;
private static String url;
private static String userName;
private static String passWord;
static {
    //读取src下的db.properties给上面的四个静态成员变量赋值
    //使用类加载器读取src下的db.properties
    InputStream inputStream =
    DButil2.class.getClassLoader().getResourceAsStream("db.properties");
    Properties pro = new Properties();
    //加载流中的key/value
    try {
        pro.load(inputStream);
        driverClassName = pro.getProperty("driverClassName");
        url = pro.getProperty("url");
        userName = pro.getProperty("userName");
        passWord = pro.getProperty("passWord");
    } catch (IOException e) {
        e.printStackTrace();
    }
    try {
        Class.forName(driverClassName);
    } catch (ClassNotFoundException e) {
        e.printStackTrace();
    }
}
```

### DAO
1. 什么是DAO:Data Access Object 数据访问对象。它是对数据访问过程封装的对象
2. 如何编写DAO
    1. 根据需求编写DAO对应的接口：返回值，方法名，参数
    2. 创建需要被返回的实体类并封装
    3. 使用DBUtil工具类结合JDBC编程的五步，重写接口中对应的方法 
    4. 测试：创建接口实现的类，调用重写后的方法，接收返回值

## Java数据存储篇--Jdbc--第3天
### JDBC事务的概念
1. 在dos命令行操作oracle时,执行DML,需要结束事务(commit提交或rollback回退)
2. 在JDBC中,事务是自动提交的,每执行一条DML语句,事务就自动提交一次. 
3. 我们可以通过JDBC的事务API,开始事务的手动提交,将多条DML语句看作一个整体,要么一起成功,要么一起失败。

### JDBC事务操作格式
1. 注意: 开启事务的手动提交,是通过连接对象完成的
    1. 某个数据连接对象的事务开启手动提交后,这个连接对象的事务需要手动控制,其他连接对象不受影响
2. 操作方法:
    1. 开始事务的手动提交:
        1. conn.setAutoCommit(boolean flag);
        2. 参数含义:true表示自动提交,false表示手动提交。
    2. 提交事务:conn.commit();
    3. 回退事务:rollback();

### 批处理(了解)
1. 将多条SQL语句 放到一起批量处理.
批处理将多次对于数据库的操作次数,减少到了一次!提高了大量SQL语句一起执行时的性能.
2. 使用步骤:
    1. 批处理使用Statement类操作
        1. 将一条SQ语句加入到批处理中:statement.addBatch(String sql);
        2. 执行批处理中的所有语句:statement.executeBatch();

### 连接池
1. 概述(熟悉)
    1. 由连接池创建连接,维护连接 
    2. 我们需要使用连接时,从连接池中获取连接
    3. 如果池中存在空闲连接,则拿去使用
    4. 如果不存在空闲连接,且池未满,则在连接池中创建新的连接使用
    5. 如果不存在空闲连接,且池已满,则排队等待空闲连接
2. 使用步骤
    1. 引入相关的jar文件
        1. dbcp:连接池的代码
        2. poll:连接池的依赖库
    2. 创建一个properties文件,描述连接池的配置,大致如下
    3. 将properties文件, 转换为Properties对象。
    4. 通过连接池工厂类(BasicDataSourceFactory),创建连接池对象 (一次程序启动, 创建一个连接池就够了)
    5. 通过连接池对象,获取池中的连接:`Connection conn = ds.getConnection();`
    6. 正常JDBC操作
    ```java
#数据库连接地址
url=jdbc:oracle:thin:@localhost:1521:XE
#数据库驱动地址
driverClassName=oracle.jdbc.OracleDriver
#数据库帐号
username=system
#数据库密码
password=123
#扩展配置:
#初始化连接池时, 创建的连接数量:
initialSize=5
#最大允许存在的连接数量
maxActive=200
#空闲时允许保留的最大连接数量
maxIdle=10
#空闲时允许保留的最小连接数量
minIdle=5
#排队等候的超时时间
maxWait=20000
    ```

### DBCPUtil工具类
```java
public class DBCPUtil {
        private static DataSource dataSource;
        static {
            //在类加载时, 读取配置文件, 配置连接池
            //1.    创建Properites对象
            Properties ppt = new Properties();
            //2.    读取配置文件, 
            InputStream is = DBCPUtil.class.getClassLoader().getResourceAsStream("dbcp.properties");
            //3.    将配置文件 加载到Properties对象中
            try {
                ppt.load(is);
            //4.    通过连接池工厂类, 创建连接池
                dataSource = BasicDataSourceFactory.createDataSource(ppt);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        /**
         * 用于从连接池中 获取一个连接对象
         * @return 连接对象 , 如果获取失败返回null
         */
        public static Connection getConnection() {
            try {
                return dataSource.getConnection();
            } catch (Exception e) {
                e.printStackTrace();
                return null;
            }
        }
        /**
         * 用于释放资源
         * @param conn  连接对象
         * @param state 执行环境
         * @param result 结果集
         */
        public static void close(Connection conn , Statement state ,ResultSet result) {
            if(result!=null) {
                try {
                    result.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(state!=null) {
                try {
                    state.close();
                } catch (SQLException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
            if(conn!=null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
        
    }
```

### 数据库优化
1. 在进行表格查询时,where子句中的条件执行顺序是从左至右,清除数据量较大的条件应该放在左边.(特别注意:笛卡尔积消除条件必须放在最左边)
2. 在进行表格查询时,列名列表应避免使用`*`号!数据库在执行查询操作时,会先将`*`号展开,转换为所有的列名,再进行查询.
3. 在进行表格查询时,能使用where条件筛选的数据,应尽量避免使用having子句来筛选.因为where条件执行在having之前,在早期筛选掉大量数据,可以让程序执行的更顺畅.
4. 在进行多表查询时,查询的表顺序是从右至左的.应把表中数据量最少的表放在查询的最右边.
5. 在进行多表查询时,应尽可能的给所有的表添加别名,能明确的区分有冲突的列.
6. 在使用事务时,应尽量多的commit,尽量早的commit!原因是:事务在未提交时,数据库会耗费大量的内存,来缓存未提交的SQL结果!
7. 尽可能多的使用函数来提高SQL执行的效率.
8. SQL语句编写时,除字符串以外,应使用大写字母!因为SQL语句执行时, 会先将小写字母转换为大写字母,再执行.
9. 应尽可能少的访问数据库(多次数据访问的结果可能相同, 如果缓存起来,可以提高程序的执行效率)
10. 在索引列上,尽可能避免使用not来判断.not关键字如果判断了索引列 , 会导致此次查询索引失效,转而使用全表扫描的方式查询.
11. 在索引列上,不能使用算数运算,算数运算也会导致索引列使用,使用全表扫描的方式进行查询.
12. 在查询数据时,如果需要使用>或<的条件,应替换为>=或<= ! 原因是>和<符号,查询时,是按照>=和<=进行查询,然后在撇去=的结果.






