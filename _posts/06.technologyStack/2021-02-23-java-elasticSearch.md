---
layout: post
title:  "ElasticSearch(v6.5.4)学习笔记"
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
```
< dependencies>
    < dependency>
        < groupId>org.elasticsearch< /groupId>
        < artifactId>elasticsearch< /artifactId>
        < version>6.5.4< /version>
    < /dependency>
    < !--es的高级api-->
    < dependency>
        < groupId>org.elasticsearch.client< /groupId>
        < artifactId>elasticsearch-rest-high-level-client< /artifactId>
        < version>6.5.4< /version>
    < /dependency>
    < dependency>
        < groupId>junit< /groupId>
        < artifactId>junit< /artifactId>
        < version>4.12< /version>
    < /dependency>
    < dependency>
        < groupId>org.projectlombok< /groupId>
        < artifactId>lombok< /artifactId>
        < version>1.16.10< /version>
    < /dependency>
< /dependencies>
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
    ```
< dependency>
    < groupId>com.fasterxml.jackson.core< /groupId>
    < artifactId>jackson-databind< /artifactId>
    < version>2.11.3< /version>
< /dependency>
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
    Map< String,Object> doc = new HashMap< >();
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
@Test//创建批量操作
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
@Test// 批量删除
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

## 5.ElasticSearch练习的准备数据
1. 索引名称:sms-logs-index
2. 索引类型:sms-logs-type   
![准备数据索引](/assets/technologyStack/elasticSearch/准备数据索引.jpg)
3. 实体类
```java
public class SmsLogs {
    @JsonIgnore
    private String id; // id

    @JsonFormat(pattern = "yyyy-MM-dd")
    private Date createDate; // 创建时间

    @JsonFormat(pattern = "yyyy-MM-dd")
    private Date sendDate; // 发送时间

    private String longCode; // 发送的长号码
    private String mobile; // 手机号
    private String corpName;  // 发送公司名称
    private String smsContent; // 短信内容
    private Integer start; // 短信发送状态,0成功，1失败
    private Integer operatorId; // 运营商编号 1移动 2联通 3电信
    private String province; // 省份
    private String ipAddr; // 服务器ip地址
    private Integer replyTotal; // 短信状态报告返回时长（秒）
    private Integer fee; // 费用
}
```
4. 创建索引
```java
 // 创建索引
@Test
public void CreateIndexForSms() throws IOException {
    // 创建索引
    Settings.Builder settings = Settings.builder()
            .put("number_of_shards", 5)
            .put("number_of_replicas", 1);
    // 指定mappings
    XContentBuilder mappings = JsonXContent.contentBuilder()
            .startObject()
                .startObject("properties")
                    .startObject("createDate")
                        .field("type", "date")
                        .field("format","yyyy-MM-dd")
                    .endObject()
                    .startObject("sendDate")
                        .field("type", "date")
                        .field("format", "yyyy-MM-dd")
                    .endObject()
                        .startObject("longCode")
                        .field("type", "keyword")
                    .endObject()
                        .startObject("mobile")
                        .field("type", "keyword")
                    .endObject()
                        .startObject("corpName")
                        .field("type", "keyword")
                    .endObject()
                        .startObject("smsContent")
                        .field("type", "text")
                        .field("analyzer", "ik_max_word")
                    .endObject()
                        .startObject("state")
                        .field("type", "integer")
                    .endObject()
                        .startObject("operatorId")
                        .field("type", "integer")
                    .endObject()
                        .startObject("province")
                        .field("type", "keyword")
                    .endObject()
                        .startObject("ipAddr")
                        .field("type", "ip")
                    .endObject()
                        .startObject("replyTotal")
                        .field("type", "integer")
                    .endObject()
                        .startObject("fee")
                        .field("type", "long")
                    .endObject()
                .endObject()
            .endObject();
    // 将settings和mappings封装为Request对象
    CreateIndexRequest request = new CreateIndexRequest(index)
            .settings(settings)
            .mapping(type,mappings);
    // 通过Client连接
    CreateIndexResponse res = client.indices().create(request, RequestOptions.DEFAULT);
    System.out.println(res.toString());
}
```
5. 创建测试数据
```java
// 测试数据
@Test
public void CreateTestData() throws IOException {
    // 准备多个json数据
    SmsLogs s1 = new SmsLogs("1",new Date(),new Date(),"10690000988","1370000001","途虎养车","【途虎养车】亲爱的刘女士，您在途虎购买的货物单号(Th12345678)",0,1,"上海","10.126.2.9",10,3);
    SmsLogs s2 = new SmsLogs("2",new Date(),new Date(),"84690110988","1570880001","韵达快递","【韵达快递】您的订单已配送不要走开哦,很快就会到了,配送员:王五，电话:15300000001",0,1,"上海","10.126.2.8",13,5);
    SmsLogs s3 = new SmsLogs("3",new Date(),new Date(),"10698880988","1593570001","滴滴打车","【滴滴打车】指定的车辆现在距离您1000米,马上就要到了,请耐心等待哦,司机:李师傅，电话:13890024793",0,1,"河南","10.126.2.7",12,10);
    SmsLogs s4 = new SmsLogs("4",new Date(),new Date(),"20697000911","1586890005","中国移动","【中国移动】尊敬的客户，您充值的话费100元，现已经成功到账，您的当前余额为125元,2020年12月18日14:35",0,1,"北京","10.126.2.6",11,4);
    SmsLogs s5 = new SmsLogs("5",new Date(),new Date(),"18838880279","1562384869","网易","【网易】亲爱的玩家,您已经排队成功,请尽快登录到网易云游戏进行游玩,祝您游戏愉快---网易云游戏",0,1,"杭州","10.126.2.5",10,2);
    // 转为json
    ObjectMapper mapper = new ObjectMapper();
    String json1 = mapper.writeValueAsString(s1);
    String json2 = mapper.writeValueAsString(s2);
    String json3 = mapper.writeValueAsString(s3);
    String json4 = mapper.writeValueAsString(s4);
    String json5 = mapper.writeValueAsString(s5);

    // request,将数据封装进去
    BulkRequest request = new BulkRequest();
    request.add(new IndexRequest(index,type,s1.getId()).source(json1,XContentType.JSON));
    request.add(new IndexRequest(index,type,s2.getId()).source(json2,XContentType.JSON));
    request.add(new IndexRequest(index,type,s3.getId()).source(json3,XContentType.JSON));
    request.add(new IndexRequest(index,type,s4.getId()).source(json4,XContentType.JSON));
    request.add(new IndexRequest(index,type,s5.getId()).source(json5,XContentType.JSON));
    // client执行
    BulkResponse response = client.bulk(request, RequestOptions.DEFAULT);
    System.out.println(response);
}
```

## 6.ElasticSearch的各种查询
### 6.1 term&terms查询
#### 6.1.1 term查询
term查询是完全匹配的，搜索之前不会对搜索的关键字进行分词，比如要搜河南省
```json
POST /sms-logs-index/sms-logs-type/_search
{
    "from": 0,   // 类似limit，指定查询第一页
    "size": 5,   // 指定一页查询几条
    "query": {
        "term": {
            "province": {
                "value": "上海"
            }
        }
    }
}
```

```java
private String index = "sms-logs-index";
private String type = "sms-logs-type";
// client对象
private RestHighLevelClient client = ESClient.getClient();
// term查询
@Test
public void termQuery() throws IOException {
    //1  request
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    //2 指定查询条件
        // 指定form ,size
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.from(0);
    builder.size(5);
         // 指定查询条件,province字段，内容为北京
    builder.query(QueryBuilders.termQuery("province","上海"));
    request.source(builder);
    //3执行查询
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    //4 获取到数据
    for (SearchHit hit : response.getHits().getHits()) {
        Map<String, Object> result = hit.getSourceAsMap();
        System.out.println(result);
    }
}
```

#### 6.1.2 terms查询
> terms查询，也是不会对条件进行分词，但是这个可以指定多条件，比如查询地点为上海的或者河南的
> * trem:where province = '北京'
> * terms:where province = '北京' or province = '上海'
```json
POST /sms-logs-index/sms-logs-type/_search
{
    "from": 0,   // 类似limit，指定查询第一页
    "size": 5,   // 指定一页查询几条
    "query": {
        "terms": {
            "province": [
                "上海",
                "北京"
            ]
        }
    }
}
```

```java
@Test
public void termsQuery() throws IOException {
    // request
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.termsQuery("province","上海","河南"));
    request.source(builder);
    // 执行查询
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取数据
    for (SearchHit hit : response.getHits().getHits()) {
        Map<String, Object> result = hit.getSourceAsMap();
        System.out.println(result);
    }
}
```

### 6.2 match查询
> match查询会根据不同的情况切换不同的策略
>
> * 如果查询date类型和数字，就会将查询的结果自动的转换为数字或者日期
> * 如果是不能被分词的内容(keyword)，就不会进行分词查询
> * 如果是text这种，就会根据分词的方式进行查询
>
> match的底层就是多个term查询，加了条件判断等
#### 6.2.1 match_all查询
会将全部的doc查询出来
```json
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "match_all": {}
  }
}
```

```java
// match_all查询
@Test
public void matchAllQuery() throws IOException {
    // request
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.matchAllQuery());
    //es默认只查询10条数据,如果想查询更多,指定size
    builder.size(20);
    request.source(builder);
    // 执行查询
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取数据
    for (SearchHit hit : response.getHits().getHits()) {
        Map<String, Object> result = hit.getSourceAsMap();
        System.out.println(result);
    }
}
```

#### 6.2.2 match查询
match查询会针对不同的类型执行不同的策略,查询text类型的数据会对条件进行分词
```json
POST /sms-logs-index/sms-logs-type/_search
{
    "query": {
        "match": {
            "smsContent": "电话"
        }
    }
}
```

```java
// match查询
builder.query(QueryBuilders.matchQuery("smsContent","电话号码"));
```

### 6.3 其他查询
#### 6.3.1 布尔match查询
可以查询既包含条件1，又包含条件2的内容，也就是and的效果，也可以实现or的效果
```json
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "match": {
      "smsContent": {
        "query": "电话 快递", 
        "operator": "and" // or
```

```java
// 布尔match查询
builder.query(QueryBuilders.matchQuery("smsContent","电话 快递").operator(Operator.AND));
```

#### 6.3.2 multi_match查询
1. 针对多个key对应一个value进行查询, 比如下面就是查询地区带中国，或者内容带中国
```json
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "multi_match": {
      "query": "中国",
      "fields": ["province","smsContent"]
```

java查询简单写，其余的部分均一样
```java
builder.query(QueryBuilders.multiMatchQuery("中国","smsContent","province"));
```

#### 6.3.3 id&ids查询
1. id查询
```json
GET /sms-logs-index/sms-logs-type/1
```

```java
// id查询
@Test
public void idMatchQuery() throws IOException {
    // 使用getRequest
    GetRequest request = new GetRequest(index,type,"1");
    // 执行查询
    GetResponse response = client.get(request, RequestOptions.DEFAULT);
    // 输出结果
    Map<String, Object> result = response.getSourceAsMap();
    System.out.println(result);
}
```

2. ids查询:给以多个id，查询多个结果，类似mysql的where id in(1,2,3.....)

```json
# ids查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "ids": {
      "values": ["1","2","3"]
```

```java
// ids查询
@Test
public void idsQuery() throws IOException {
    // 这个属于复杂查询需要使用searchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.idsQuery().addIds("1","2","3"));

    request.source(builder);
    // 执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 输出结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

#### 6.3.4 prefix查询
1. 听名字就是前缀查询，查询字首的，可以指定指定字段的前缀，从而查询到指定的文档，可以实现类似百度输入后弹出提示的效果
```json
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "prefix": {
      "corpName": {
        "value": "滴滴"  // 这样就能搜到所有关于滴滴开头的公司名称了
```

```java
// prefix查询
@Test
public void prefixQuery() throws IOException {
    // 依然使用SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.prefixQuery("corpName","滴滴"));
    request.source(builder);
    // 执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

#### 6.3.5 kuzzy查询
模糊查询，根据输入的内容大概的搜索，可以输入错别字，不是很稳定，比如输入`网一`来搜索`网易`就搜不到
```json
# fuzzy查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "fuzzy": {
      "corpName": {
        "value": "中国移不动",
         "prefix_length": 2  // 可选项，可以指定前几个字符是不能错的
```

```java
// fuzzy查询
@Test
public void fuzzyQuery() throws IOException {
    // 依然使用SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.fuzzyQuery("corpName","中国移不动"));
    //builder.query(QueryBuilders.fuzzyQuery("corpName","中国移不动").prefixLength(2));
    request.source(builder);
    // 执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

#### 6.3.6 wildcard查询
通配查询，和mysql的`like`是一个套路，可以在搜索的时候设置占位符，通配符等实现模糊匹配

```json
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "wildcard": {
      "corpName": {
        "value": "中国*" // *代表通配符,?代表占位符 ，比如:中国? 就是搜中国开头的三个字的内容
```

```java
// wildcard查询
@Test
public void wildcardQuery() throws IOException {
    // 依然使用SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.wildcardQuery("corpName","中国??"));
    request.source(builder);
    // 执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

#### 6.3.7 range查询
> 范围查询，只针对数值类型

这里的范围是`带等号`的，这里能查询到fee等于5，或者10的,如果想要`<`或者`>`的效果可以看注释

```json
# range查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "range": {
      "fee": {
        "gte": 5,  //gt
        "lte": 10  //lt
```

这里的范围，指定字符串的5或者int类型的5都是可以的，es会自动的进行转换

```java
// range查询
@Test
public void rangeQuery() throws IOException {
    // 依然使用SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.rangeQuery("fee").gte("5").lte("10"));
    request.source(builder);
    // 执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

#### 6.3.8 regexp查询
> 正则查询，通过编写的正则表达式匹配内容
>
> * PS：prefix，fuzzy，wildcard，regexp，查询的效率相对比较低，要求效率高的时候，不要使用这个

```json
# regexp查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "regexp": {
      "mobile": "15[0-9]{8}" // 这里查询电话号码15开头的，后面的数字8位任意
```

```java
// regexp查询
@Test
public void regexpQuery() throws IOException {
    // 依然使用SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 查询
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.regexpQuery("mobile","15[0-9]{8}"));
    request.source(builder);
    // 执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

### 6.4 解决深分页的方案sroll
> 针对term查询的from和size的大小有限制，from+size的总和不能大于1万
>
> from+size查询的步骤:
> * 第一步:先进行分词
> * 第二步:然后把词汇去分词库检索，得到文档的id
> * 第三步:然后去分片中把数据拿出来
> * 第四步:然后根据score进行排序
> * 第五步:然后根据from和size`舍弃一部分`
> * 第六步:最后将结果返回
>
> scroll+size查询的步骤:
> * 第一步:先进行分词
> * 第二步:然后把词汇去分词库检索，得到文档的id
> * 第三步:将文档的id存放唉es的上下文中(内存中)
> * 第四步:根据指定的size去es中拿指定数量的数据，拿完数据的docId会从上下文移除
> * 第五步:如果需要下一页数据，会去es的上下文中找
>
> **scroll也有缺点，不适合实时查询，因为是从内存中找以前查询的，拿到的数据不是最新的，这个查询适合做后台管理**

```json
POST /sms-logs-index/sms-logs-type/_search?scroll=1m  // 这里指定在内存中保存的时间，1m就是1分钟
{
  "query": {
    "match_all": {}
  },
  "size": 2,
  "sort": [   // 这里指定排序规则
    {
      "fee": {
        "order": "desc"
      }
    }
  ]
}
```
查询下一页的数据
```json
POST /_search/scroll
{
  "scroll_id":"这里写id", // 这里写上第一次查询的_scroll_id
  "scroll":"1m"   // 重新指定存在时间，否则直接从内存删除了
}
```
如果看完第二页不想看下去了，想直接删除掉内存中的数据：
```json
DELETE /_search/scroll/scroll的id
```

```java
// scroll查询
@Test
public void scrollQuery() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 指定scroll的信息，存在内存1分钟
    request.scroll(TimeValue.timeValueMinutes(1L));
    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.size(1);
    builder.sort("fee", SortOrder.ASC);
    builder.query(QueryBuilders.matchAllQuery());
    request.source(builder);
    // 执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取第一页的结果结果，以及scrollId
    String scrollId = response.getScrollId();
    System.out.println("------第一页------");
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }

    // 循环遍历其余页
    while (true){
        // SearchScrollRequest,指定生存时间,scrollId
        SearchScrollRequest scrollRequest = new SearchScrollRequest(scrollId);
        scrollRequest.scroll(TimeValue.timeValueMinutes(1L));
        // 执行查询
        SearchResponse scrollResponse = client.scroll(scrollRequest, RequestOptions.DEFAULT);

        // 如果查询到了数据
        SearchHit[] hits = scrollResponse.getHits().getHits();
        if (hits !=null && hits.length>0){
            System.out.println("------下一页------");
            for (SearchHit hit : hits) {
                System.out.println(hit.getSourceAsMap());
            }
        }else {
            System.out.println("-----最后一页-----");
            break;
        }
    }
    // ClearScrollRequest
    ClearScrollRequest clearScrollRequest = new ClearScrollRequest();
    clearScrollRequest.addScrollId(scrollId);
    // 删除ScoreId
    ClearScrollResponse scrollResponse = client.clearScroll(clearScrollRequest, RequestOptions.DEFAULT);

    System.out.println("删除scroll成功了吗？"+scrollResponse.isSucceeded());
}
```

### 6.5 delete-by-query
> 根据term,match等查询方式删除大量的文档
>
> [如果是大量的删除，不推荐这个方式，太耗时了，因为是根据查询的id一个一个删除，而查询本身也很消耗性能，推荐新建一个index，把保留的部分保留到新的index]( )

```json
POST /sms-logs-index/sms-logs-type/_delete_by_query   // 把查询出来的结果删除
{
  "query":{
    "range":{
      "fee":{
        "lt":4
```

```java
// deleteByQuery查询
@Test
public void deleteByQuery() throws IOException {
    // DeleteByQueryRequest
    DeleteByQueryRequest request = new DeleteByQueryRequest(index);
    request.types(type);

    // 指定检索条件
    request.setQuery(QueryBuilders.rangeQuery("fee").lt(4));

    // 执行删除
    BulkByScrollResponse response = client.deleteByQuery(request, RequestOptions.DEFAULT);

    System.out.println(response);
}
```

### 6.6 复合查询
#### 6.6.1 bool查询
> 将多个查询条件以一定的逻辑组合在一起
>
> * must：表示and的意思，所有的条件都符合才能找到
> * must_not：把满足条件的都去掉的结果
> * should：表示or的意思

```json
// 查询省份是上海或者河南
// 运营商不是联通
// smsContent中包含中国和移动
// bool查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": { 
    "bool":{
      "should": [ // or
        {
          "term": {
            "province": {
              "value": "上海"
            }
          }
        },
        {
          "term": {
            "province": {
              "value": "河南"
            }
          }
        }
      ],
      "must_not": [ // 不包括
        {
          "term": {
            "operatorId": {
              "value": "2"
            }
          }
        }
      ],
      "must": [ // and
        {
          "match": {
            "smsContent": "中国"
          }
        },
        {
          "match": {
            "smsContent": "移动"
          }
        }
      ]
    }
  }
}
```

```java
// boolQuery查询
@Test
public void boolQuery() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    BoolQueryBuilder boolQuery = QueryBuilders.boolQuery();
    // 上海或者河南
    boolQuery.should(QueryBuilders.termQuery("province","武汉"));
    boolQuery.should(QueryBuilders.termQuery("province","河南"));
    // 运营商不是联通
    boolQuery.mustNot(QueryBuilders.termQuery("operatorId",2));
    // 包含中国和移动
    boolQuery.must(QueryBuilders.matchQuery("smsContent","中国"));
    boolQuery.must(QueryBuilders.matchQuery("smsContent","移动"));
    // 指定使用bool查询
    builder.query(boolQuery);
    request.source(builder);

    // client执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);

    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

#### 6.6.2 boolsting
> 分数查询，查询的结果都是有匹配度一个分数，可以针对内容，让其分数大，或者小，达到排前，排后的效果
>
> * `positive`： 只有匹配到positive的内容，才会放到结果集，也就是放查询条件的地方
> * `negative`：如果匹配到的positive和negative，就会降低文档的分数source
> * `negative_boost`：指定降低分数的系数，必须小于1.0，比如：10分 这个系数为0.5就会变为5分
>
> 关于分数的计算：
>
> * 关键字在文档出现的频次越高，分数越高
> * 文档的内容越短，分数越高
> * 搜索时候，指定的关键字会被分词，分词内容匹配分词库，匹配的个数越多，分数就越高

```json
# boosting查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "boosting": {
      "positive": {
        "match": {
          "smsContent": "亲爱的"
        }
      },
      "negative": {
        "match": {
          "smsContent": "网易"
        }
      },
      "negative_boost": 0.5
    }
  }
}
```

```java
// boostingQuery查询
@Test
public void boostingQuery() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    BoostingQueryBuilder boostingQueryBuilder = QueryBuilders.boostingQuery(
        QueryBuilders.matchQuery("smsContent", "亲爱的"),
        QueryBuilders.matchQuery("smsContent", "网易")
    ).negativeBoost(0.5f);
    builder.query(boostingQueryBuilder);
    request.source(builder);
    // client执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);
    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

### 6.7 filter查询
> 过滤器查询：根据条件去查询文档，不会计算分数，而且filter会对经常查询的内容进行缓存
>
> 前面的query查询：根据条件进行查询，计算分数，根据分数进行排序，不会进行缓存

```json
//filter查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "bool":{
      "filter": [  // 过滤器可以指定多个
        {
          "term":{
            "corpName": "中国移动"
            }
        },
        {
          "range":{
            "fee": {
              "lte": 5
            }
          }
        }]
    }
  }
}

```

```java
// filterQuery查询
@Test
public void filterQuery() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);
    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    BoolQueryBuilder boolQuery = QueryBuilders.boolQuery();
    boolQuery.filter(QueryBuilders.termQuery("corpName","中国移动"));
    boolQuery.filter(QueryBuilders.rangeQuery("fee").lte(5));

    builder.query(boolQuery);
    request.source(builder);
    // client执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);

    // 获取结果
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

### 6.8 高亮查询
> 将用户输入的内容，以高亮的样式展示出来，查询的结果会附带在hits下面以单独的形式返回，不会影响查询的结果
>
> ES提供了一个`hightlight`的属性，和`query`同级别，其属性如下：
>
> * `fragment_size`：指定要展示多少内容，可以看到百度的内容后面有...还有很长，默认`100个`
> * `pre_tags`：指定前缀标签  比如：<font color="red">就是红色
> * `post_tags`：指定后缀标签：</font>
> * `fields`：指定哪几个field以高亮形式返回

```json
# hight查询
POST /sms-logs-index/sms-logs-type/_search
{
  "query": {
    "match": {   // 查询
      "smsContent": "亲爱的"
    }
  },
  "highlight": {   // 高亮显示
    "fields": {
      "smsContent": {}  // 要高亮展示的内容
    },
    "pre_tags": "<font color=red>", 
    "post_tags": "</font>",
    "fragment_size": 10
  }
}
```

```java
// highlightQuery查询
@Test
public void highlightQuery() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);

    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.query(QueryBuilders.matchQuery("smsContent", "亲爱的"));
    // 高亮显示
    HighlightBuilder highlightBuilder = new HighlightBuilder();
    highlightBuilder.field("smsContent",10) // 只显示10个字
        .preTags("<font color='read'>").postTags("</font>");    // 红色展示

    builder.highlighter(highlightBuilder);
    request.source(builder);
    // client执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);

    // 获取结果,拿高亮的内容
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getHighlightFields());
    }
}
```

### 6.9 聚合查询
> 也就是类似mysql的count，max，avg等查询，但要更为强大
聚合查询有新的语法

```json
POST /index/type/_search
{
    "aggs":{
        "名字(agg)":{
            "agg_type":{
                "属性":"值"
            }
        }
    }
}
```

#### 6.9.1 去重计数查询
> 去掉重复的数据，然后算出总数，也就是`Cardinality`

```json
// 去重记数查询
POST /sms-logs-index/sms-logs-type/_search
{
  "aggs": {
    "agg": { // 这个名字任意，不过会影响查询结果的键
      "cardinality": {   // 去重查询
        "field": "province"
```

可以看到我命名的是`agg`，这里查询的键也是`agg`

```java
// 去重记数查询
@Test
public void cardinalityQuery() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);

    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.aggregation(AggregationBuilders.cardinality("agg").field("province"));
    request.source(builder);
    // client执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);

    // 获取结果,拿到总数,因为Aggregation是一个接口，我们需要向下转型，使用实现类的方法才能拿的value
    Cardinality agg = response.getAggregations().get("agg");
    long value = agg.getValue();
    System.out.println("省份总数为："+value);

    // 拿到查询的内容
    for (SearchHit hit : response.getHits().getHits()) {
        System.out.println(hit.getSourceAsMap());
    }
}
```

#### 6.9.2 范围统计

> 根据某个属性的范围，统计文档的个数，
>
> 针对不同的类型指定不同的方法，
>
> `数值`：range
>
> `时间`：date_range
>
> `ip`：ip_range

数值范围查询：
```json
# 范围统计查询，小于号是不带等号的
POST /sms-logs-index/sms-logs-type/_search
{
  "aggs": {
    "agg": {
      "range": {
        "field": "fee",
        "ranges": [       
          {
            "to": 5  // 小于5
          },
          {
            "from": 6,  // 大于等于6，小于10
            "to": 10
          },
          {
            "from":10  // 大于等于10 
          }
        ]
      }
    }
  }
}
```

时间范围查询

```json
# 时间范围统计查询
POST /sms-logs-index/sms-logs-type/_search
{
  "aggs": {
    "agg": {
      "date_range": {
        "field": "createDate",
        "format": "yyyy",   // 指定查询条件，这里是以年为条件
        "ranges": [
          {
            "to": "2000"  // 小于2000年
          },
          {
            "from": "2000"  // 大于等于2000年
          }
        ]
      }
    }
  }
}
```

ip范围查询

```json
# ip范围统计查询
POST /sms-logs-index/sms-logs-type/_search
{
  "aggs": {
    "agg": {
      "ip_range": {
        "field": "ipAddr",
        "ranges": [
          {
            "from": "10.126.2.7",  // 查询这个范围的ip
            "to": "10.126.2.10"
          }
        ]
      }
    }
  }
}
```

```java
// 范围统计查询
@Test
public void range() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);

    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.aggregation(AggregationBuilders.range("agg").field("fee")
                        .addUnboundedTo(5)   // 指定范围
                        .addRange(5,10)
                        .addUnboundedFrom(10));

    request.source(builder);
    // client执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);

    // 获取结果
    Range agg = response.getAggregations().get("agg");
    for (Range.Bucket bucket : agg.getBuckets()) {
        String key = bucket.getKeyAsString();
        Object from = bucket.getFrom();
        Object to = bucket.getTo();
        long docCount = bucket.getDocCount();
        System.out.println(String.format("key：%s，from：%s，to：%s，docCount：%s",key,from,to,docCount));
    }
}
```

#### 6.9.3 统计聚合查询
> 可以查询属性(`field`)的最大值，最小值，平均值，平方和.......

```json
POST /sms-logs-index/sms-logs-type/_search
{
  "aggs": {
    "agg": {
      "extended_stats": {
        "field": "fee"
      }
    }
  }
}
```

```java
// 聚合查询
@Test
public void extendedStats() throws IOException {
    // SearchRequest
    SearchRequest request = new SearchRequest(index);
    request.types(type);

    // 指定查询条件
    SearchSourceBuilder builder = new SearchSourceBuilder();
    builder.aggregation(AggregationBuilders.extendedStats("agg").field("fee"));

    request.source(builder);
    // client执行
    SearchResponse response = client.search(request, RequestOptions.DEFAULT);

    // 获取结果
    ExtendedStats agg = response.getAggregations().get("agg");
    double max = agg.getMax();
    double min = agg.getMin();

    System.out.println("fee的最大值为"+max);
    System.out.println("fee的最小值为"+min);
}
```

[其余的详情访问官网非常全面](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/getting-started.html)