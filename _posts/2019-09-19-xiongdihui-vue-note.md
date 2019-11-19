---
layout: post
title:  "Vue学习笔记"
date:   2019-09-19
categories: Vue
tags: Vue note
---

* content
{:toc}

Vue学习笔记






# Vue学习笔记
1. 实例化
```
new Vue{
    ml:'#id',
    data:{
        name:tiankai,
        age:18
    }
}
```

2. 绑定方法
```
methods:{
    greet:function(){
        this.age == ;
    }
}
```

3. 事件
```
v-on:click //v-on：需要触发的事件
v-bind:herf    //v-bind:给属性绑定对应的值
```

4. 事件修饰符
```
.stop:
.once:
.prevent:
```

5. 键盘事件  
```
v-on:keyup='事件名'
```

6. 可获取输入的标签
```
input textarea select
通过ref获取，给input加一个ref标签，起个名字例如rfs="name"
this.name=this.$refs.name.value
或者直接v-model="name"
这样就获取到了
```

7. 计算属性
```
computed:
因为methods里，每调用一次它执行所有的方法
而computed只执行对应的方法，调用时方法名花括号里不加小括号
```

8. `v-if` +`v-for`
`v-if="属性名"`  
`<li v-for="x in 数组名">`  
    `{``{``x``}``}`  
`</li>`  



