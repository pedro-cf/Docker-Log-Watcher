docker build -t docker_log_watcher .
docker run -p 883:5000 -v /var/run/docker.sock:/var/run/docker.sock docker_log_watcher
