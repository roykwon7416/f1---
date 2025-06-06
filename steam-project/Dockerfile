FROM python:3.11-slim
WORKDIR /app

# 백엔드 의존성
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r backend/requirements.txt

# 소스 복사
COPY backend /app/backend
COPY frontend /app/frontend

# 서버 실행
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]