FROM python:3.10-alpine
RUN apk update
WORKDIR /app
COPY /src/tetraplex/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY /src/tetraplex/server.py /app/server.py
CMD ["python", "/app/server.py"]
