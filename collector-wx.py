import requests
import logging
import subprocess
import time
from threading import Timer
from lxml import etree

def download(name, url):
    cmd = ['curl', '--connect-timeout', '8', '-m', '12', '-o', name, url]
    getit = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    timer = Timer(13, lambda process: process.kill(), [getit])
    try:
        timer.start()
        stdout, stderr = getit.communicate()
    finally:
        timer.cancel()
    if isinstance(stdout, str) and len(stdout):
        return stdout
    else:
        return []

def getHtml():
    cookies = { #此处 cookies 替换成你自己未过时的 cookie 一般 几小时就过期了
            'PHPSESSID':'nvudbmma7gpjhdk4ldp2r07c41',
            '_csrf':'4e153b9c5950a65252bd5a11e4fdb85b631ea040abd85f502957bdb259254ce0a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%228sobThwO3GdTnhXaR6g5x3w_FqZFtJaW%22%3B%7D',
            '__cfduid':'db3385d1e8468a44d6ae9dead0bb033c11522771606',
            'Hm_lvt_10e35f8c37b477709b953c2cca2f57f6':'1522742810',
            'Hm_lpvt_10e35f8c37b477709b953c2cca2f57f6':'1522841936'
    }
    agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400'
    headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Host': 'wx.oinbag.com',
            'User-Agent': agent
        }
    url = 'http://wx.oinbag.com/index.php/baota/index-load-more?tmi=546727&page='
    #循环获取多页
    for n in range(1,3):
        urls = url + str(n)
        html_respont = requests.post(urls, cookies = cookies, headers = headers)
        #print(html_respont.text)
        html = etree.HTML(html_respont.text)
        img1 = html.xpath('//div[@class="img-list-container"]/ul/li[@class="event-img-file"]/@path')
        #print(img1)
        img1_name = html.xpath('//div[@class="event-container"]/div/a[@class="car-no"]/text()')
        print(img1_name)
        j = 0
        previous = ''
        for i in range(len(img1)):
            event_num = img1[i][36:43]
            print(event_num)
            print(previous)
            if event_num == previous:
                j = j+1
                print(j)
                previous = event_num
            else:
                j = 0
            image_url = img1[i]
            #image_url = image_url[:image_url.find("x-oss")-1]
            download("./plates/"+'_'+str(i)+"_"+img1_name[j]+'.jpg',str(image_url))
            logging.critical('download '+img1_name[j]+'_'+str(i)+'.jpg')
                

getHtml()