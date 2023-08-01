FROM python:3.10-slim
COPY ./GoEmotions /app
COPY ./requirements_Lin.txt /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements_Lin.txt
EXPOSE 8080
ENTRYPOINT ["python", "app-gcp.py"]