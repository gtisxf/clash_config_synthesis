# -*- coding: utf-8 -*-

import requests #导入requests模块
import yaml #导入yaml模块
from datetime import datetime

# 获取当前时间.写入配置文件前
now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")
header = f"""
# 该配置文件由代码自动生成
# 生成时间: {date_str}
"""

url1 = "https://1.cn/1.yaml"
url1 = "https://2.cn/2.yaml"


headers = {'User-Agent': 'ClashX Pro/1.90'}  
#设置一个ClashX的User-Agent,一些provider可能会要求

resp1 = requests.get(url1, headers=headers) 
#使用headers发送GET请求获取第一个yaml文件
resp2 = requests.get(url2, headers=headers)
#同样方式获取第二个yaml文件

yaml1 = yaml.load(resp1.text, Loader=yaml.FullLoader)
#使用yaml模块加载第一个yaml文本
yaml2 = yaml.load(resp2.text, Loader=yaml.FullLoader) 
#同样方式加载第二个

# print(type(yaml1['proxies']))
# print(yaml1['proxies'])

# print(type(yaml2['proxies'])) 
# print(yaml2['proxies'])about:blank#blocked



yaml1['proxies'].extend(yaml2['proxies'])
#将第二个yaml的proxies合并到第一个yaml里面

#提取name
name_list = []
for proxy in yaml2['proxies']:
    name = proxy['name']
    name_list.append(name)

yaml1['proxy-groups'][2]['proxies']=name_list

# print(type(yaml1['proxy-groups'])) 
# print(yaml1['proxy-groups'])

with open('clash.yaml', 'w') as f:
    f.write(header+yaml.dump(yaml1)) #转字符串后写入
