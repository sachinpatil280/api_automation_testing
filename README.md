# API Testing Assignment

## Overview
This project is used to test a given API with "GET" method. The automation uses Python with `requests` library and using pytest framework.
Test cases are specified in `test_cases` folder and `pytest-html` library is used for generating report.


## Installation and running on the local machine
To do the setup on local machine, please follow the below steps:

Navigate to `configurations` folder and run below command to install dependencies:
```
pip install -r requirements.txt
```
Navigate to root of the project and run below command to run the tests:
```
sh run_test.sh
```

## Validating the reports

Reports are generated in `results` folder.

## Creating docker image using `Dockerfile` from root directory and running docker tests 

Running below command will run tests on docker and the results will be copied to host machine's "results" folder.

```
sh run_docker_tests.sh
```