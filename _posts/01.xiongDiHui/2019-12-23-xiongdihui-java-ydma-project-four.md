---
layout: post
title:  "Java猿代码学习平台4"
date:   2019-12-23
categories: Project
tags: project
---

* content
{:toc}

1. Java猿代码学习平台4：SpringBoot访问Redis操作




## Redis优点
1. 异常快速,每秒可以执行大约110000设置操作,81000个读取操作
2. 支持丰富的数据类型,例如列表,集合,可排序集合,哈希等数据类型
3. 支持数据的持久化,Redis提供了一些策略将内存中的数据异步地保存到磁盘上,比如根据时间或更新次数
4. Redis是一个多功能实用工具,具有缓存、消息传递等功能

## Redis命令
1. Redis命令-1

字符串操作命令|功能描述
--|--
set key value|此命令用于在置顶键设置值
get key|键对应的值
getset key value|设置键的字符串值,并返回旧值
strlen key|得到存储在键的值的长度
mset key value [key value...]|设置多个键和多个值
incr key|键的整数值加1
incrby key value|键的整数值加value
decr key|键的整数值减1
decrby key value|键的整数值减value
append key value|为原来键值追加value

2. Redis管理命令-2

管理键的命令|功能描述
--|--
del key|此命令删除键,如果存在
exists key|此命令检查该键是否存在
expire key seconds|指定键的过期时间
pexpire key milliseconds|设置键以毫秒为单位到期
persist key|移除过期的键
keys pattern|查找与指定模式匹配的所有键
dump key|该命令返回存储在指定键的值的序列化结果
randomkey|从redis返回随机键
rename key newkey|更改键的名称
type key|返回存储在键的数据类型的值
pttl key|以毫秒为单位获取剩余时间的到期键
ttl key|获取键到期的剩余时间

3. Redis哈希操作命令

哈希操作命令|功能描述
--|--
hmset key field1 value1[field2 value2]|设置多个哈希字段的多个值
hset key field value|设置哈希字段的字符串值
hget key field|获取存储在指定的键散列字段的值
hmget key field1[field2]|获取所有给定的哈希字段的值
hlen key|设置多个建和多个值
hkeys key|获取所有哈希表中的字段
hdel key field2|删除对应的属性值
hexists key field|查询是否存在,1存在,0不存在

4. 列表操作命令

列表操作命令|功能描述
--|--
lpush key value1[value2]|在前面加上一个或多个值的列表
rpush key value1[value2]|在末尾加上一个或多个值的列表
lrange key start stop|返回存储在key列表的特定元素
llen key|获取列表的长度
lpop key|从头部删除一个元素,并返回删除的元素
rpop key|从尾部删除一个元素,并返回删除的元素

5. 无序集合操作命令

集合操作命令|功能描述
--|--
sadd key member[member...]|向集合增加元素
srem key member[member...]|从集合删除元素
smembers key|获得集合中的所有元素
sismember key member|判断元素是否在集合中
scard key|获得集合中元素的个数
srandmember key [count]|随机获得集合中的元素
spop key|从列表中弹出一个元素,并删除

6. 有序集合操作命令

有序集合操作命令|功能描述
--|--
zadd key score1 member1[score2 member2]|向有序集合添加一个或多个成员.或者更新已存在成员的分数
zcard key|获取有序集合的成员数
zcount key min max|计算在有序集合中指定区间分数的成员数
zscore key member|获取元素的分数
zrange key start stop[withscores]|通过索引区间返回有序集合成指定区间内的成员(小到大)
zrevrange key start stop[withscores]|通过索引区间返回有序集合成指定区间内的成员(大到小)
zrangebyscore key score1 score2|根据排序索引的scores来返回元素

7. 事务操作命令
    1. MULTI : 开启事务操作
    2. EXEC : 将加入队列的操作执行
    3. DISCARD : 撤销
    4. SAVE : 该命令将在redis安装目录中创建dump.rgb文件
    5. BGSAVE : 创建redis备份文件也可以使用命令BGSAVE,该命令在后台执行
    6. CONFIG GET dir : 获取redis安装目录,数据恢复时只需要将导出的dump.rgb文件移动到redis安装目录并启动服务即可

## SpringBoot访问Redis操作

在spring-data-redis工具有一个RedisTemplate对象，可以使用该对象对redis操作。

对jedis的API进行了封装，对象序列化和反序列化进行了封装。

1. 在原始Spring框架中配置RedisTemplate

```xml
<bean id="redisFactory" class="org.springframework.data.redis.connection.jedis.JedisConnectionFactory">
    <property name="hostName" value="192.168.95.128"></property>
    <property name="port" value="6379"></property>
</bean>

<bean id="redisTemplate" class="org.springframework.data.redis.core.RedisTemplate">
    <property name="connectionFactory" ref="redisFactory"></property>
    <property name="keySerializer">
        <bean class="org.springframework.data.redis.serializer.StringRedisSerializer"/>
    </property>
</bean>
```

2. 在SpringBoot框架中使用方法

- 在pom.xml引入spring-boot-starter-data-redis启动器
- 在application.properties定义redis访问参数
- 通过自动配置会创建RedisTemplate对象，直接注入使用

```java
@Autowired
private RedisTemplate<Object, Object> redisTemplate;

@Override
public YdmaResult loadCourse(int id) {
YdmaResult result = new YdmaResult();
//先查询Redis缓存
Course course = (Course)redisTemplate.opsForValue().get("course:"+id);
if(course == null) {
    //缓存没有，再调用dao查询DB
    course = courseDao.selectByPrimaryKey(id);
    //将查询的course放入Redis缓存
    redisTemplate.opsForValue().set("course:"+id, course);
    System.out.println("从DB查询");
}

if(course != null) {
    result.setCode(YdmaConstant.SUCCESS);
    result.setMsg(YdmaConstant.LOAD_SUCCESS_MSG);
    result.setData(course);
}else {
    result.setCode(YdmaConstant.ERROR1);
    result.setMsg(YdmaConstant.LOAD_ERROR1_MSG);
}
    return result;
}
```

## Redis存储和读取对象原始方法

1. 工具类

```java
public class SerializedUtil {
    /**
     *  将对象转成字节数组
     * @param obj
     * @return
     * @throws Exception
     */
    public static byte[] objToBytes(Object obj) throws Exception {
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream out = new ObjectOutputStream(bos);
        out.writeObject(obj);
        byte[] bytes = bos.toByteArray();
        out.close();
        bos.close();
        return bytes;
    }
    /**
     *  将字节数组转成对象
     * @param bytes
     * @return
     * @throws Exception
     */
    public static Object bytesToObject(byte[] bytes) throws Exception {
        ByteArrayInputStream bis = new ByteArrayInputStream(bytes);
        ObjectInputStream in = new ObjectInputStream(bis);
        Object obj = in.readObject();
        in.close();
        bis.close();
        return obj;
    } 
}
```

2. 将对象存入redis

```java
public void test5() throws Exception {
    Direction direction = new Direction();
    direction.setId(1);
    direction.setName("前端开发");
    //写入redis
    Jedis jedis = new Jedis("localhost", 6379);
    byte[] value = SerializedUtil.objToBytes(direction);
    jedis.set("direction1".getBytes(),value);
    jedis.close();
}
```

3. 从redis中取出对象

```java
public void test6() throws Exception {
    Jedis jedis = new Jedis("localhost", 6379);
    byte[] value = jedis.get("direction1".getBytes());
    Direction d = (Direction)SerializedUtil.bytesToObject(value);
    System.out.println(d.getId()+" "+d.getName());
    jedis.close();
}
```

4. 原理
    1. 其实就是将对象转换成字节数组存入到redis,取出的时候再将字符数组转换成对象
    2. 存入redis的对象必须实现Serializable序列化接口,因为在将对象转换成字符数组的时候用到对象输出流,对象输出流写入的时候,要求被写入的对象实现序列化接口











