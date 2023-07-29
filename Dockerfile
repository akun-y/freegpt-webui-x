# 基于Ubuntu镜像构建
FROM ubuntu:20.04 AS build

#替换为阿里源
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.aliyun.com/#' /etc/apt/sources.list \
    && sed -i 's#http://security.ubuntu.com/#http://mirrors.aliyun.com/#' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y python3 python3-pip

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install --user --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

FROM build AS prod
WORKDIR /app
# COPY client ./client
# COPY g4f ./g4f
# COPY server ./server
# COPY run.py ./
# 使用.dockerignore
COPY . ./

EXPOSE 1338/tcp

CMD [ "python3", "run.py" ]