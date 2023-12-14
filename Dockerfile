# 使用精简镜像，镜像体积从 1.2G 下降为约 400M，提高启动效率，同时升级到 Python 3.11.x 提高 20% 以上性能
FROM python:3.11-slim-bullseye

# 升级 pip 到最新版
RUN pip install --upgrade pip

COPY  ./ /usr/local/aktools
WORKDIR /usr/local/aktools

# 安装nodejs
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt-get install -y nodejs

RUN pip install -r requirements.txt
# 新增 gunicorn 安装，提升并发和并行能力
RUN pip install --no-cache-dir gunicorn -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade
WORKDIR /usr/local/aktools/aktools
# 默认启动 gunicorn 服务
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app", "-k", "uvicorn.workers.UvicornWorker"]
