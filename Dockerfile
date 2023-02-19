FROM python:3.9-slim-buster AS base
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

FROM base
COPY . /app
EXPOSE 5000
WORKDIR app
ENTRYPOINT [ "python", "app.py" ]
