# Docker Log Watcher

Docker Log Watcher is a simple web application that allows you to view the logs of your Docker containers in a web page. It provides a read-only view of your logs, which can be shared with other people without granting them access to your Docker environment.

## Usage

To use Docker Log Watcher, you need to build and run the Docker image provided in this repository. Here are the steps to follow:

1. Clone this repository to your local machine:

   '''bash
   git clone https://github.com/pedro-cf/docker_log_watcher.git
   '''

2. Change to the cloned directory:

   '''bash
   cd docker_log_watcher
   '''

3. Build the Docker image:

   '''
   docker build -t docker_log_watcher .
   '''

4. Run the Docker container:

   '''
   docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock docker_log_watcher
   '''

   This command starts a Docker container that listens on port 5000 and mounts the Docker socket to access the logs of other containers on the host machine.

5. Access the logs in your web browser:

   Open a web browser and navigate to `http://localhost:5000/`. You will see a web page with a drop-down list of the containers running on your machine. Select a container to view its logs.

   The logs are displayed in a scrolling text area, with the most recent logs at the top. The logs are refreshed every second to show the latest changes.

## Requirements

Docker Log Watcher requires the following:

* Docker (the application uses the Docker API to fetch the container logs)
* Python 3
* Flask

## License

Docker Log Watcher is released under the MIT License. See the [LICENSE](LICENSE) file for details.
