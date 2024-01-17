FROM python:3.11.7-slim

WORKDIR /app

# 프로젝트 파일을 컨테이너에 복사
RUN pip install "poetry==1.7.1"
COPY pyproject.toml poetry.lock* ./

# 의존성 설치
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction

RUN useradd --create-home appuser

WORKDIR /home/appuser
USER appuser

COPY --chown=appuser:appuser . .

# FastAPI 서버 실행.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
