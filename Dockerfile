FROM python:3.13-slim
WORKDIR /server

COPY . .

EXPOSE 5000/tcp

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
