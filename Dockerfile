FROM python:3.9-slim-buster
RUN pip install flask docker
COPY . /
EXPOSE 5000
ENTRYPOINT [ "python", "/app.py" ]
