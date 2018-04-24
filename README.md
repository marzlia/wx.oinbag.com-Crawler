# python 爬取 wx.oinbag.com 上面的车牌图片

## 1.开发需求

偶然在做车牌识别的过程中，要做机器学习，但苦于没有数据，就得到了这个 www.oinbag.com,而它的微信公众号上面才有更多的数据可以获取，wx.oinbag.com 地址，所以产生了爬取数据的想法

>https://github.com/szad670401/oinbagCrawler

这位大哥给出了先例爬取了 www.oinbag.com，但是 wx.oinbag.com 数据才更多，于是产生了这个项目


## 2.环境搭建工具配置

要用到的工具包含但不限于以下：
```
1.微信桌面客户端（windows 客户端才能访问公众号里面的内容）
2.Fiddler 抓包获取 cookie
3.python 3
4.chrome 或者 firefox
```

## 3.完成功能

- [ ] cookie自动获取
- [ ] 对应图片的车牌号
- [ ] 提取图片地址备份到csv文件
- [ ] 获取每页地址
- [x] 微信浏览器伪装
- [x] 带有header与cookie请求
- [x] cookie手动fiddler提取