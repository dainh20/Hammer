FROM ubuntu:22.04

# Chống treo khi cài đặt và tối ưu Python
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Cài đặt system packages (bao gồm thư viện cho Kafka và Postgres)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev \
    # Công cụ mạng & debug cho DE
    git curl vim nano iputils-ping net-tools \
    # Công cụ cho Kafka & Redis & DB
    librdkafka-dev \
    redis-tools \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Alias python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Upgrade pip
RUN pip install --upgrade pip

# Working directory
WORKDIR /app

# Copy requirements và cài đặt (Tận dụng Docker Cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Tạo user devuser và phân quyền cho thư mục app
RUN useradd -ms /bin/bash devuser && chown -R devuser /app
USER devuser

# Giữ container chạy để vọc vạch (dev mode)
CMD ["sleep", "infinity"]