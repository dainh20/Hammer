FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev \
    git curl vim nano iputils-ping net-tools \
    librdkafka-dev \
    redis-tools \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install --upgrade pip

WORKDIR /app

# cài dependencies trước (cache tốt)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY . .

# tạo user
RUN useradd -ms /bin/bash devuser && chown -R devuser /app
USER devuser

# expose port FastAPI
EXPOSE 8000

# chạy API
CMD ["sleep", "infinity"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]