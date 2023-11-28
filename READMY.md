# Automated testing API using Python and the `requests` library.


## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Common Issues](#usage)


## Description

This project is designed to perform testing on the Deezer API using Python and the requests library. It contains tests for Artist and Search endpoints.

The [Deezer API](https://developers.deezer.com/api) is a comprehensive platform that allows developers to access various music-related data, including artists, tracks, albums, and more. The `requests` library, integrated into this project, enables the retrieval and verification of data from the Deezer API for the purpose of automated testing.

This project is built using Python, a high-level programming language known for its simplicity and readability. Python offers a robust and extensive standard library and has a thriving community that contributes to its development and support. For more information on Python, visit the official Python website: [Python Official Website](https://www.python.org/)

One of the key components of this project is the `requests` library, a powerful Python library designed for making HTTP requests. serves a main role in interacting with the [Deezer API](https://developers.deezer.com/api), providing uninterrupted communication for creating automated test cases. For detailed information about the `requests` library, refer to the [Requets Documentation](https://docs.python-requests.org/en/master/).

This project uses the Selenium WebDriver, a popular tool for automating web applications for testing purposes. Selenium provides a user-friendly API that enables the interaction with various web elements, making it an ideal choice for web testing and automation tasks. To learn more about Selenium WebDriver, refer to the Selenium documentation: [Selenium Documentation](https://www.selenium.dev/documentation/en/)


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

3. Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

Make sure you have Python and pip installed on your machine before running the project. You can integrate this project into your to automate the testing process. Please share details and commands related to your usage.


## Usage

### Running Tests

Execute the tests using the preferred test runner. For example, using pytest:

    ```bash
	pytest tests
    ```
	
### Adding New Tests

To add new tests, follow these guidelines:

1. Create a new test file in the tests/ directory.
2. Name the file starting with test_.
3. Write individual test functions within the file.
	
### Test Configuration

Adjust the test configuration, such as test data, in the config.ini file.


## Common Issues

If you encounter any issues while running or contributing to the project, check the Common Issues section in this README.

