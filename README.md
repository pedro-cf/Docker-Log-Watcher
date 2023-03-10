# Docker Log Watcher

Docker Log Watcher is a simple web application that allows you to view the logs of your Docker containers in a web page. It provides a read-only view of your logs, which can be shared with other people without granting them access to your Docker environment.

![image](https://user-images.githubusercontent.com/4175430/220098454-7a307bae-551d-4250-8ddf-68b0b0e50dc0.png)


## Usage

To use Docker Log Watcher, you need to build and run the Docker image provided in this repository. Here are the steps to follow:

1. Clone this repository to your local machine:

```
git clone https://github.com/pedro-cf/docker_log_watcher.git
```

2. Change to the cloned directory:

```
cd docker_log_watcher
```

3. Build the Docker image:

```
docker build -t docker_log_watcher .
```

4. Run the Docker container:

```
docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock -e BASIC_AUTH_USERNAME=<username> -e BASIC_AUTH_PASSWORD=<password> docker_log_watcher [container_name1] [container_name2] ...
```

This command starts a Docker container that listens on port 5000 and mounts the Docker socket to access the logs of other containers on the host machine. It also sets the BASIC_AUTH_USERNAME and BASIC_AUTH_PASSWORD environment variables to the desired username and password for basic authentication. You can optionally pass container names as arguments to the Docker command to filter which containers to display.

5. Access the logs in your web browser:

Open a web browser and navigate to `http://localhost:5000/`. You will see a web page with a drop-down list of the containers running on your machine. Select a container to view its logs.

The logs are displayed in a scrolling text area, with the most recent logs at the bottom. The logs are refreshed every second to show the latest changes.

You filter the logs by text by entering a search term in the "Filter" text input. The logs will be updated to show only the lines that match the search term.

You can export logs to text by pressing the "Export Logs" button.

## Requirements

Docker Log Watcher requires the following:

* Docker

## License

Docker Log Watcher is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you find this project useful, consider buying me a coffee! Donations help keep this project going and are greatly appreciated.

[![Buy me a coffee](https://img.shields.io/badge/-Buy%20me%20a%20coffee-orange?logo=buy-me-a-coffee&logoColor=white&style=for-the-badge)](https://www.buymeacoffee.com/pedro_cf)
