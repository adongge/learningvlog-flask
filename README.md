# learningvlog-flask
flask 学习笔记
---
参考：https://dormousehole.readthedocs.io/en/latest/index.html

## c1
- flask 安装
    1. python3.x 虚拟环境，独立库 ,并启用虚拟环境
    2. 安装 flask 
    3. 创建app.py 运行flask 


## c2
- 配置环境和日志
    1. 安装 pip install python-dotenv
    2. 创建.env 文件配置当前环境为开发环境 FLASK_ENV=development 和 environment.py 文件 写入 ENV='Development'

    3. 新建文件夹 Config ，文件夹内创建 Development.py 
    4. 日志配置信息写到 Development.py 中
    5. 修改 app.py 文件，完成相关日志代码
    6. 运行调试


## c3
- 使用 uwsgi 运行flask
    1. 安装 pip install uwsgi
    2. 配置 uwsgi.dev.ini 文件
    3. 运行 venv/bin/uwsgi uwsgi.dev.ini
    4. 😏😏😏完成


```ini

[uwsgi]
chdir=/Users/adong/learning/learningvlog-flask/c3
wsgi-file = /Users/adong/learning/learningvlog-flask/c3/app.py
home=/Users/adong/learning/learningvlog-flask/venv
callable = app
http = 127.0.0.1:5000

```

## c4
- 蓝图 blueprint
    1. 创建Base目录 整理app.py代码放到Base 中
    2. 创建App目录 存放蓝图 blueprint请求代码
    3. 创建blueprint.py 注册创建的蓝图
    4. 😂done


## c5
- 前后端分离，统一返回json响应格式
    1. 创建类JSONEncoder.py 转换部分需要的python对象为json
    修改app JSONEncoder处理对象 😀done
    2. 创建类APIResponse.py 返回固定格式json
    3. 创建api_route.py 将1、2 过程交由 api_route.py处理，不用每次return重复编写，默认返回统一是json格式的数据
    



















## c6 
- 前后端分离，统一异常/错误响应格式
    2. 