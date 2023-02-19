import docker
from flask import Flask, render_template, request, jsonify
from flask_basicauth import BasicAuth
import os, sys

app = Flask(__name__)
app.config["BASIC_AUTH_USERNAME"] = os.environ.get("BASIC_AUTH_USERNAME")
if app.config["BASIC_AUTH_USERNAME"] is None:
    raise Exception("BASIC_AUTH_USERNAME not defined")
app.config["BASIC_AUTH_PASSWORD"] = os.environ.get("BASIC_AUTH_PASSWORD")
if app.config["BASIC_AUTH_PASSWORD"] is None:
    raise Exception("BASIC_AUTH_PASSWORD not defined")
basic_auth = BasicAuth(app)
client = docker.from_env()


@app.route("/")
@basic_auth.required
def index():
    containers = client.containers.list()
    container_names = [container.name for container in containers]
    if len(sys.argv) > 1:
        container_names = filter(lambda x: x in sys.argv[1:], container_names)
    return render_template("index.html", container_names=container_names)


@app.route("/logs")
@basic_auth.required
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
