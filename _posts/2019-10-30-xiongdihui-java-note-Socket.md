---
layout: post
title:  "使用ServerSocket类和Socket类实现服务器与客户端的连接"
date:   2019-10-30
categories: Java
tags: Java note
---

* content
{:toc}

使用ServerSocket类和Socket类实现服务器与客户端的连接










## 1.服务器端
```java
import java.net.ServerSocket;
import java.net.Socket;
public class ServerTest {
    public static void main(String[] args) {
        try {
//          1.创建一个ServerSocket对象并提供端口号
            ServerSocket ss = new ServerSocket(8888);
//          循环监听接入的客户端
            while(true){
//              2.监听客户端连接
                System.out.println("等待客户端连接ing");
                Socket s = ss.accept();
//                获取连接成功的客户端的通信地址
                System.out.println("客户端"+s.getInetAddress()+"连接成功！！！");
//                将新连接的客户端分配给新线程服务
                new ServerThread(s).start();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
```

## 2.自定义一个类实现每个新线程
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;
public class ServerThread extends Thread {
    private Socket s;
    public ServerThread(Socket s){
        this.s=s;
    }
    @Override
    public void run() {
        try{
//          3.使用输入输出流进行通信
            BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintStream ps = new PrintStream(s.getOutputStream());
            while(true){
//                接收客户端消息并打印
                String s1 = br.readLine();
                System.out.println("客户端"+s.getInetAddress()+":"+s1);
                if (s1.equals("bye")){
                    System.out.println("客户端"+s.getInetAddress()+"已下线");
                    break;
                }
//                自动回复消息给客户端
            ps.println("I received!");
            System.out.println("服务端发送数据成功");
            }
//          4.关闭Socket
            ps.close();
            br.close();
            s.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
```

## 3.客户端
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Scanner;
public class ClientTest {
    public static void main(String[] args) {
        try {
//      1.创建Socket对象
            Socket s = new Socket("服务器的IP地址,或者计算机名",8888);
            System.out.println("客户端连接成功！！！");
//      2.使用输入输出流进行通信
            PrintStream ps = new PrintStream(s.getOutputStream());
            BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
            Scanner sc = new Scanner(System.in);
//            循环向服务器发送数据，直到发送"bye"才停止
            while(true) {
//            向服务器发送数据
                System.out.println("请输入要发送的信息:");
                String s1 = sc.nextLine();
                ps.println(s1);                
                if (s1.equals("bye")){
                    System.out.println("聊天结束");
                    break;
                }else{
                    System.out.println("客户端发送数据成功");
                }
//            接收服务器发回的数据
                String s2 = br.readLine();
                System.out.println(s2);
            }
//      3.关闭Socket
            br.close();
            ps.close();
            s.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```









