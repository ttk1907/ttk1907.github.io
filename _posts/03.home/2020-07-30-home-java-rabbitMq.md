---
layout: post
title:  "RabbitMQ入门"
date:   2020-07-30
categories: messageQueue
tags: rabbitmq
---

* content
{:toc}

1. RabbitMQ入门





# RabbitMQ入门
## 一、RabbitMQ运行机制
1. AMQP中的消息队列
AMQP中增加了`Exchange`和`Binding`的角色.生产者把消息发布到交换机上,消息最终到达队列并被消费者接收,而Binding绑定规则则决定交换机的消息应该发送到哪一个队列.
2. Exchange类型
    1. direct模式 : 点对点类型,根据路由键将消息发送到对应的队列中
    2. fanout模式 : 发布订阅模式,将接收到的消息发送到每一个绑定的消息队列中
    3. topic模式 : 模糊匹配型,topic交换器通过模式匹配,将路由键和某个模式进行匹配,此时队列需要绑定到一个模式上.它将路由键和绑定建的字符串切分成单词,这些单词用点隔开.符号`#`和符号`*`,`#`匹配0个或多个单词,`*`号匹配一个单词
        1. 例如:可以绑定`user.#`,可以匹配到`user`和`user.ttk`
    4. headers模式 : 根据header信息匹配而不是路由键,header交换器和direct交换器完全一致,但性能差很多,目前几乎用不到

## 二、SpringBoot整合RabbitMQ
1. 添加依赖

```java
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

2. 自动配置
    1. RabbitAutoConfiguration.java是springboot自动配置rabbitmq的文件
        1. springBoot自动配置了连接工厂
        2. 封装了RabbitMq的配置
        3. 配置了RabbitTemplate,用来给rabbitmq发送和接收消息
        4. 配置了AmqpAdmin,用来管理rabbitMQ
        5. 使用`@RabbitListener`来监听队列中的消息

3. 常用方法
    1. RabbitTemplate的convertAndSend方法用来向消息队列中发送消息
    2. RabbitTemplate的receiveAndConvert方法用来接收消息
    3. AmqpAdmin中有创建交换器和队列还有绑定规则的方法
    ```java
    @Test
    public void contextLoads() {
        rabbitTemplate.convertAndSend("exchange.ttk.direct","ttk.nb",new Book("小黄书","ttk"));
    }

    @Test
    public void receive(){
        Object o = rabbitTemplate.receiveAndConvert("ttk");
        System.out.println(o.getClass());
        System.out.println(o);
    }
    ```

4. 接收消息

    1. springBoot中使用@RabbitListener注解来接收消息
    ```java
    //接收实体类
    @RabbitListener(queues = "ttk")
    public void revice(Book book){
        System.out.println("收到消息"+book);
    }
    //接收消息体
    @RabbitListener(queues = "ttk.nb")
    public void revice02(Message message){
        System.out.println(Arrays.toString(message.getBody()));
        System.out.println(message.getMessageProperties());
    }
    ```
