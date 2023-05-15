# use Python 3.10 to match Streamlit Cloud for testing since they haven't upgraded yet (5/6/2023)
FROM python:3.10-slim  
LABEL maintainer="Brandon Corfman @bcorfman"

EXPOSE 8501

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/bcorfman/bfs.git

WORKDIR /bfs

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"] 
