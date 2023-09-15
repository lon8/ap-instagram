FROM python:3.9

WORKDIR /app
COPY ./instagram-service /app

RUN pip install fastapi uvicorn requests

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000"]