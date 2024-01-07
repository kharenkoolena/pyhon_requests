# Automated API Testing with Python and Requests Library


## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Test Configuration](#test-configuration)
- [Usage with Docker](#usage-with-docker)
- [Usage without Docker](#usage-without-docker)
- [Common Issues](#common-issues)


## Description

This project is designed to perform testing on the Deezer API using Python and the requests library. It contains tests for Artist and Search endpoints.

The [Deezer API](https://developers.deezer.com/api) is a comprehensive platform that allows developers to access various music-related data, including artists, tracks, albums, and more.

This project is built using Python, a high-level programming language known for its simplicity and readability. Python offers a robust and extensive standard library and has a thriving community that contributes to its development and support. For more information on Python, visit the official Python website: [Python Official Website](https://www.python.org/)

One of the key components of this project is the `requests` library, a powerful Python library designed for making HTTP requests. serves a main role in interacting with the [Deezer API](https://developers.deezer.com/api), providing uninterrupted communication for creating automated test cases. For detailed information about the `requests` library, refer to the [Requets Documentation](https://docs.python-requests.org/en/master/).

## Installation

To use this project, follow these steps:

1. Clone the repository to your local machine using the following command:

    ```bash
	https://github.com/kharenkoolena/python_requests.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-project
    ```
	
## Test Configuration

Adjust the test configuration, such as test data, in the config.ini file:

1. Open the `config.ini` file located in the project directory.

2. Update the relevant configurations as necessary.


## Usage with Docker

It is recommended to use Docker to ensure a consistent environment and ease of deployment. Docker allows you to isolate the project's dependencies, making it straightforward to run across different systems.

1. Download and Install Docker:

   Make sure you have Docker installed on your machine. If not, you can download it [here](https://www.docker.com/products/docker-desktop/).

2. Build Docker Image (Container):

    ```bash
    docker build -t my_python_requests_app .
    ```
	
3. Run Docker Container:

    ```bash
    docker run my_python_requests_app
    ```
	
By using Docker, you benefit from reproducibility and avoid potential compatibility issues.

## Usage without Docker

While Docker is recommended for its simplicity and consistency, you can also run the project without it. Follow these steps:

1. Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

Make sure you have Python and pip installed on your machine before running the project. You can integrate this project into your to automate the testing process. Please share details and commands related to your usage.

2. Run tests using the preferred test runner. For example, using pytest:

    ```bash
	pytest tests
    ```
	
3. To add new tests, follow these steps:

	1. Create a new test file in the tests/ directory.
	2. Name the file starting with test_.
	3. Write individual test functions within the file.


## Common Issues

If you encounter any issues or have questions, feel free to open an issue for further assistance.
