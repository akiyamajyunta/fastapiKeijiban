# python3.9のイメージをダウンロード
FROM python:3.9-buster

WORKDIR /workspace

RUN mkdir /workspace/api

COPY api ./
COPY requirements.txt ./ /workspace/


RUN pip install -r requirements.txt
RUN cd api
# uvicornのサーバーを立ち上げる
CMD ["python", "main.py"]