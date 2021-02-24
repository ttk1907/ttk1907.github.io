---
layout: post
title:  "ElasticSearch学习笔记"
date:   2021-02-23
categories: technologyStack
tags: technologyStack note
---

* content
{:toc}

1. ElasticSearch介绍
2. ElasticSearch安装
3. ElasticSearch基本操作
4. java操作ElasticSearch
5. ElasticSearch练习
6. ElasticSearch的各种查询






# ElasticSearch学习笔记

## 1.ElasticSearch介绍
### 1.1 引言
1. 在海量数据中执行搜索功能时,如果使用mysql,效率太低。
2. 如果将关键字输入的不准确,一样可以搜索到想要的数据。
3. 将搜索关键字以红色的字体展示。

### 1.2 ES的介绍
1. ES是一个使用Java语言并且基于Lucene编写的搜索引擎框架,他提供了分布式的全文搜索功能,提供了一个统一的基于RESTful风格的WEB接口,官方客户端也对多种语言都提供了相应的API。
2. Lucene:Lucene本身就是一个搜索引擎的底层。
3. 分布式:ES主要是为了突出它的横向扩展能力
4. 全文检索**(倒排索引)**:将一段词语进行分词,并且将分出来的单个词语统一的放到一个分词库中,在搜索时,根据关键字去分词库中检索,找到匹配的内容。
5. ReSTful风格的WEB接口:操作ES很简单,只需要发送一个HTTP请求,并且根据请求的方式不同,携带参数的不同,执行相应的功能。
6. 应用广泛:Github.com,WIKI,Gold Man用ES每天维护将近10TB的数据

### 1.3 ES和Slor的比较
1. Solr在查询死数据时,速度相对ES更快一些。但是数据如果是实时改变的,Solr的查询速度会降低很多,ES的查询的效率基本没有变化。
2. Solr搭建集群需要Zookeeper来帮助管理,ES本身就支持集群的搭建,不需要第三方的介入。
3. 最开始Solr的社区可以说是非常火爆,针对国内的文档并不是很多。在ES出现之后,ES的社区火爆程度直线上升,ES的文档非常健全。
4. ES对现在云计算和大数据的支持特别好。

### 1.4 倒排索引     
![倒排索引](/assets/technologyStack/elasticSearch/倒排索引.jpg)
1. 将存放的数据以一定的方式进行分词,并且将分词的内容存放到一个单独的分词库中。
2. 当用户去查询数据时,会将用户的查询关键字进行分词,然后去分词库中匹配内容,最终得到数据的id标识。
3. 根据id标识去存放数据的位置拉取指定的数据。

## 2.ElasticSearch安装
1. [安装ES、Kibana、ik分词器](http://dl.elasticsearch.cn/),在该网站下载解压即可,ik分词器解压到es文件夹下的plugins/ik文件夹中   
![ik分词器效果](/assets/technologyStack/elasticSearch/ik分词器.jpg)

## 3.ElasticSearch基本操作
### 3.1 ES的结构
1. 索引index   
![索引index](/assets/technologyStack/elasticSearch/索引index.jpg)
    1.  ES的服务中可以创建多个索引，
    2.  每个索引默认分成5片存储，
    3.  每一个至少有一个备份分片
    4.  备份分片正常不会帮助检索数据，除非ES的检索压力很大的情况发送
    5.  如果只有一台ES，是不会有备份分片的，只有搭建集群才会产生
2. 类型type   
![type结构](/assets/technologyStack/elasticSearch/type结构.jpg)
    1. ES 5.x下，一个index可以创建多个type
    2. ES 6.x下，一个index只能创建一个type
    3. ES 7.x下，直接舍弃了type，没有这玩意了
3. 文档doc   
![文档结构](/assets/technologyStack/elasticSearch/文档结构.jpg)
    1. 一个type下可以有多个文档doc，这个doc就类似mysql表中的行
4. 属性field   
![field结构](/assets/technologyStack/elasticSearch/field结构.jpg)
    1. 一个doc下可以有多个属性field，就类似于mysql的一列有多行数据

### 3.2 操作ES的RESTful语法
1. GET请求:
    1. http://ip:port/index:查询索引
    2. http://ip:port/index/type/doc_id:查询文档
2. POST请求:
    1. http://ip:port/index/type/\_search:查询文档,可在请求体中添加json字符串代表查询条件
    2. http://ip:port/index/type/doc_id/\_update:
3. PUT请求:修改文档,在请求体中添加json字符串指定修改的具体信息
    1. http://ip:port/index:创建一个索引,需要在请求体中指定索引的信息,类型,结构
    2. http://ip:port/index/type/\_mappinngs:代表创建索引时,指定索引文档存储的属性的信息
4. DELETE请求:
    1. http://ip:port/index:删除跑路
    2. http://ip:port/index/type/doc_id:删除指定文档

### 3.3 索引的操作
1. 创建索引   
```json   
// 1 创建名为parson的索引
PUT /parson
{
  "settings": {
    "number_of_shards": 5,      // 默认分片为5
    "number_of_replicas": 1    // 默认备份为1
  }
}
```  
2. 查看索引信息
    1. management中的index Management查看
    2. 使用`GET /parson`命令查看
3. 删除索引
    1. management中的index Management查看后选中个对应索引删除
    2. 使用`DELETE /parson`命令删除

### 3.4 ES中Field可以指定的类型
1. string字符串类型:
    1. text:最常用，一般用于全文检索，会给fleld分词
    2. keyword:不会给fleld进行分词
2. number数值类型:
    1. long
    2. integer
    3. short
    4. byte
    5. double
    6. float
    7. half_float: 精度比float小一半，float是32位，这个是16位
    8. scaled_float: 根据long类型的结果和你指定的secled来表达浮点类型：long:123 ,secled:100，结果：1.23
3. date时间类型:
    1. date: 可以指定具体的格式 ,"format": "yyyy-MM-dd HH:mm:ss\|\|yyyy-MM-dd\|\|epoch_millis"
4. boolean布尔类型
    1. boolean: 表达true或false 
5. binary二进制类型
    1. binary: 基于base64的二进制
6. range范围类型
    1. long_range: 赋值时,无需指定一个具体的内容,只需要存储一个范围即可,指定gt,lt,gte,lte
    2. integer_range: 同上
    3. double_range: 同上
    4. float_range: 同上
    5. data_range: 同上
    6. ip_range: 同上
7. geo经纬度类型
    1. geo_point: 存储经纬度
8. ip类型
    1. ip: 可以存储v4,v6都可以

### 3.5 创建索引并指定数据结构
```json   
PUT /book
{
  "settings": {
    "number_of_shards": 5,   //分片数
    "number_of_replicas": 1  //备份数
  },
  "mappings": {   //指定数据结构
    "novel":{    //类型type
      "properties":{ //文档存储的field
        "name":{    //filed属性名
          "type":"text",  //类型
          "analyzer":"ik_max_word",//指定分词器
          "index":true,      //指定当前field可以被作为查询的条件
          "store":false      //是否需要额外存储
        },
        "author":{
          "type":"keyword"
        },
        "count":{
          "type":"long"
        },
        "onSale":{
          "type":"date",
          //时间类型的格式化方式
          "format":"yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"  
        },
        "descr":{
          "type":"text"
        }
      }
    }
  }
}
```   

### 3.6 文档的操作
文档在ES服务中的唯一标识,`_index, _type, _id`三个内容为组合,锁定一个文档,操作时添加还是修改
1. 新建文档
    1. 自动生成id   
    ```json
#添加文档,自动生成id
POST /book/novel
{
  "name":"盘龙",
  "author":"我吃西红柿",
  "count":1000000,
  "on-sale": "1935-01-01",
  "descr": "描述"
}
    ```   
    2. 手动指定id   
    ```json
#添加文档,手动指定id
PUT /book/novel/1
{
  "name": "三体",
  "author": "刘慈欣",
  "count": 20000,
  "on-sale": "1935-01-01",
  "descr": "给文明以岁月"
}
    ```   
2. 修改文档
    1. 覆盖式修改
    ```json
#修改文档,手动指定id
PUT /book/novel/1
{
  "name": "三体",
  "author": "刘慈欣",
  "count": 123456,
  "on-sale": "1935-01-01",
  "descr": "给文明以岁月"
}
    ```    
    2. doc修改   
    ```json
POST /book/novel/1/_update
{
    "doc": {   // 里面指定要修改的键值
        "name": "西游记"
    }
}
    ```   
3. 删除文档
    1. `Delete /book/novel/_id`

## 4.java操作ElasticSearch
### 4.1 Java连接ES
1. 创建Maven工程
2. 导入依赖   
```xml
<dependencies>
    <dependency>
        <groupId>org.elasticsearch</groupId>
        <artifactId>elasticsearch</artifactId>
        <version>6.5.4</version>
    </dependency>
    <!--es的高级api-->
    <dependency>
        <groupId>org.elasticsearch.client</groupId>
        <artifactId>elasticsearch-rest-high-level-client</artifactId>
        <version>6.5.4</version>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <version>1.16.10</version>
    </dependency>
</dependencies>
```   
3. 连接测试   
```java
public static RestHighLevelClient  getClient(){
    // 指定es服务器的ip,端口
    HttpHost httpHost = new HttpHost("192.168.10.106",9200);
    RestClientBuilder builder = RestClient.builder(httpHost);
    RestHighLevelClient client = new RestHighLevelClient(builder);  // 如果连接失败会报错，
    return client;
}
```   

### 4.2 Java创建索引
1. 创建索引   
```java
public class Demo2 {
    private RestHighLevelClient client = ESClient.getClient();
    private String index = "person";
    private String type = "man";

    @Test
    public void createIndex() throws IOException {
        //1.准备关于索引的settings
        Settings.Builder settings = Settings.builder()
        .put("number_of_shards", 5)
        .put("number_of_replicas", 1);
        //2.准备关于索引的结构mappings
        XContentBuilder mappings = JsonXContent.contentBuilder()
        .startObject()
          .startObject("properties")
               .startObject("name")
                  .field("type","text")
               .endObject()
               .startObject("age")
                 .field("type","integer")
               .endObject()
               .startObject("birthday")
                  .field("type","date")
                  .field("format","yyyy-MM-dd")
               .endObject()
           .endObject()
        .endObject();
        //3.将settings和mappings封装为Request对象
        CreateIndexRequest request = new CreateIndexRequest(index)
            .settings(settings)
            .mapping(type,mappings);
        //4.通过client对象去连接es并创建索引
        CreateIndexResponse res = client.indices().create(request, RequestOptions.DEFAULT);
        System.out.println(res.toString());
    }
}
```     
2. 检查索引是否存在   
```java
// 检查索引是否存在
@Test
public void exists() throws IOException {
    // 准备request对象
    GetIndexRequest request = new GetIndexRequest();
    request.indices(index);

    // 通过client对象操作
    boolean exists = client.indices().exists(request, RequestOptions.DEFAULT);
    // 输出,
    System.out.println(exists);
}
```     
3. 删除索引    
这里结果拿不拿到无所谓，因为删除失败直接就抛异常了
```java
// 删除索引
@Test
public void deleteIndex() throws IOException {
    // 准备request对象
    DeleteIndexRequest request = new DeleteIndexRequest();
    request.indices(index);

    //通过client对象操作
    AcknowledgedResponse delete = client.indices().delete(request, RequestOptions.DEFAULT);
    
    // 拿的是否删除成功的结果,是个布尔类型的值
    System.out.println(delete.isAcknowledged());
}
```   

### 4.3 Java操作文档
1. 添加文档
    1. 这里需要操作json,因此引入jackson    
    ```xml
<!--jackson-->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.11.3</version>
</dependency>
    ```   
    2. 准备一个实体类,因为，es的`id`是在路径上的，因此不需要存储**@JsonIgnore**注解忽略这个属性，然后将Data类型转为es的这种类型**@JsonFormat(pattern = "yyyy-MM-dd")**注解    
    ```java
public class Person {
    @JsonIgnore
    private Integer id;
    private String name;
    private Integer age;
    @JsonFormat(pattern = "yyyy-MM-dd")
    private Date birthday;
}
    ```   
    3. doc创建    
    ```java
private RestHighLevelClient client = ESClient.getClient();
private String index = "person";
private String type = "man";
// 文档创建
@Test
public void createDoc() throws IOException {
    // jackson
    ObjectMapper mapper = new ObjectMapper();
    // 1 准备一个json数据
    Person person = new Person(1,"张三",20,new Date());
    String json = mapper.writeValueAsString(person);
    // 2 request对象,手动指定id，使用person对象的id
    IndexRequest request = new IndexRequest(index,type,person.getId().toString());
    request.source(json, XContentType.JSON);//第二个参数告诉他这个参数是json类型
    // 3 通过client操作
    IndexResponse response = client.index(request, RequestOptions.DEFAULT);
    // 4 创建成功返回的结果
    String result = response.getResult().toString();
    System.out.println(result); // 成功会返回 CREATED
}
    ```   
2. 修改文档   
```java
// 文档修改
@Test
public void updateDoc() throws IOException {
    // 1 创建一个map
    Map<String,Object> doc = new HashMap<>();
    doc.put("name","李四");
    String docId = "1";
    // 2 创建一个request对象，指定要修改哪个，这里指定了index，type和doc的Id,也就是确定唯一的doc
    UpdateRequest request = new UpdateRequest(index, type, docId);
    // 指定修改的内容
    request.doc(doc);
    // 3 client对象执行
    UpdateResponse update = client.update(request, RequestOptions.DEFAULT);
    // 4 执行返回的结果
    String result = update.getResult().toString();
    System.out.println(result); // 返回结果为 UPDATE
}
```   
3. 删除文档   
```java
// 删除文档
@Test
public void deleteDoc() throws IOException {
    // 创建request,指定我要删除1号文档
    DeleteRequest request = new DeleteRequest(index, type, "1");
    // 通过client执行
    DeleteResponse delete = client.delete(request, RequestOptions.DEFAULT);
    // 获取执行结果
    String result = delete.getResult().toString();
    System.out.println(result); // 返回结果为 DELETED
}
```   

### 4.4 Java批量操作文档
1. 批量添加   
```java
// 创建批量操作
@Test
public void bulkCreateDoc() throws IOException {
    // 准备多个json数据
    Person p1 = new Person(1,"张三",22,new Date());
    Person p2 = new Person(2,"李四",22,new Date());
    Person p3 = new Person(3,"王五",22,new Date());
    // 转为json
    ObjectMapper mapper = new ObjectMapper();
    String json1 = mapper.writeValueAsString(p1);
    String json2 = mapper.writeValueAsString(p2);
    String json3 = mapper.writeValueAsString(p2);
    // request,将数据封装进去
    BulkRequest request = new BulkRequest();
    request.add(new IndexRequest(index,type,p1.getId().toString()).source(json1,XContentType.JSON));
    request.add(new IndexRequest(index,type,p2.getId().toString()).source(json2,XContentType.JSON));
    request.add(new IndexRequest(index,type,p3.getId().toString()).source(json3,XContentType.JSON));
    // client执行
    BulkResponse response = client.bulk(request, RequestOptions.DEFAULT);

}
```    
2. 批量删除   
```java
// 批量删除
@Test
public void bulkDeleteDoc() throws IOException {
    BulkRequest request = new BulkRequest();
    // 将要删除的doc的id添加到request
    request.add(new DeleteRequest(index,type,"1"));
    request.add(new DeleteRequest(index,type,"2"));
    request.add(new DeleteRequest(index,type,"3"));
    // client执行
    client.bulk(request,RequestOptions.DEFAULT);
}
```     

## 5.ElasticSearch练习
## 6.ElasticSearch的各种查询





