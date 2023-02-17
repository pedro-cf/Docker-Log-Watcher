import docker
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
client = docker.from_env()


@app.route("/")
def index():
    containers = client.containers.list()
    container_names = [container.name for container in containers]
    return render_template("index.html", container_names=container_names)


@app.route("/logs")
def logs():
    try:
        container_name = request.args.get("container_name")
        container = client.containers.get(container_name)
        logs = container.logs(tail=500, stream=False).decode("utf-8")
        return logs  # jsonify(logs=logs)
    except (docker.errors.NotFound, docker.errors.NullResource):
        return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0")
