FROM python:3.7

COPY requirement.txt /home/

RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
echo 'Asia/Shanghai' >/etc/timezone && \
pip install -r /home/requirement.txt -i https://pypi.douban.com/simple/

EXPOSE 5000

CMD ["uwsgi","/Users/adong/learning/learningvlog-flask/uwsgi.dev.ini"]


# docker build -t flask:1.0 ./
# docker images
# docker run -it --name flask -p 5000:5000 -v /Users/adong/learning/learningvlog-flask:/Users/adong/learning/learningvlog-flask:rw flask:1.0 
