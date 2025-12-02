FROM ubuntu:22.04

# 避免交互式安装提示
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# 安装基础工具和Python
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip \
    python3-venv \
    wget \
    curl \
    unzip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . .

RUN export KMP_DUPLICATE_LIB_OK=TRUE \
    && curl -fsSL https://pixi.sh/install.sh | sh \
    && echo 'export PATH="/root/.pixi/bin:$PATH"' >> /etc/profile.d/pixi.sh

ENV PATH="/root/.pixi/bin:$PATH"

RUN chmod +x chrome_setup.sh \
    && ./chrome_setup.sh

RUN pixi install

#RUN chmod +x setup.sh \
#    && ./setup.sh