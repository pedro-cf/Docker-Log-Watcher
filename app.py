import docker
from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)
client = docker.from_env()


@app.route("/")
def index():
    containers = client.containers.list()
    container_names = [container.name for container in containers]
    if len(sys.argv) > 1:
        container_names = filter(lambda x: x in sys.argv[1:], container_names)
    return render_template("index.html", container_names=container_names)


@app.route("/logs")
def logs():
    try:
        container_name = request.args.get("container_name")
        filter_pattern = request.args.get("filter")
        container = client.containers.get(container_name)
        logs = container.logs(tail=500, stream=False, timestamps=True).decode("utf-8")
        if filter_pattern:
            logs = filter(lambda x: filter_pattern in x, logs.split("\n"))
            logs = "\n".join(logs)
        return logs
    except (docker.errors.NotFound, docker.errors.NullResource):
        return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
