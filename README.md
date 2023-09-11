# clash_config_synthesis


## 作用
具有多个clash订阅，切换使用比较麻烦，使用此脚本可以在远端定时合成一个clash.yaml文件，方便直接调用。

## 使用方法
  ### 1、前置条件
  #### 准备多个订阅地址：
  
  #订阅1
  
  url1 = "https://1.cn" 
  
  #订阅2
  
  url2 = "https://2.cn"

  #下载脚本
  
  clash_config_synthesis.py
  ### 2、运行

```
  python3 clash_config_synthesis.py
```
## 说明
以下内容需要手动插入订阅1（自己的配置文件），在运行脚本之前处理完毕。
```
# 执行自动插入
- name: "yifengNodes" # 目标代理组名，对应网站配置的 group 字段
  type: url-test
  proxies: [] # 筛选后的节点将被追加至此处
  url: "http://www.gstatic.com/generate_204"
  interval: 7200

```
以下内容需要手动插入订阅1（自己的配置文件）
```
proxy-groups:
- name: "PROXY"
  type: select
  proxies:
    # - "自动选择快速节点"
    # - "ss"
    # - "ss-obfs"


- name: "autoNodes"
  type: url-test
  proxies:
    # - "ss"
    # - "ss-obfs"
    # - "ss-v2ray"
  url: 'http://www.gstatic.com/generate_204'
  interval: 7200

# 执行自动插入的位置
- name: "yifengNodes" 
  type: url-test
  proxies: [] #执行自动插入的接入列表
  url: "http://www.gstatic.com/generate_204"
  interval: 7200

```

