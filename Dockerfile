FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    fastapi \
    uvicorn \
    boltz

WORKDIR /src

COPY . /src

RUN pip install --no-cache-dir .

EXPOSE 18000

CMD ["uvicorn", "boltz_fastapi:app", "--host", "0.0.0.0", "--port", "18000"]