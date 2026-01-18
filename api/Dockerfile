# Stage 1: Builder
FROM python:3.10-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Stage 2: Runtime
FROM python:3.10-slim
RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY app.py .

USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
