---
layout: post
title:  "JS学习笔记2"
date:   2019-08-29
categories: JS
tags: JS note
---

* content
{:toc}

JS学习笔记
1. JS定时器

2. JS制作轮播图





# JS学习笔记第二天
## 1.JS定时器
```
<script type="text/javascript">
setInterval('alert("adsf")',3000);
setTimeout('alert("adsf")',3000);
</script>
```
## 2.JS制作轮播图
```
<body >
<div style="margin: 0 auto;width: 1000px;">
    <img src="/home/ttk/图片/1.jpg" id="tp" width="1000px"  >
</div>
<script type="text/javascript">
    var i = 2;
    function change(){
        imgsrc = '/home/ttk/图片/'+i+'.jpg';
        i++;
        if (i == 5){
            i=1;
        }
        document.getElementById('tp').src = imgsrc;
        

    }
setInterval('change()',1000);
</script>
</body>
```














































