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