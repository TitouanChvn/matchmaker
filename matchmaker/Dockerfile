
FROM python:latest


WORKDIR /server


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


EXPOSE 5000


CMD ["python", "server.py"]
