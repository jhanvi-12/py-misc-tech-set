<!-- Python LOGO -->
<br />
<div align="center">
   <img src="python_logo.png" alt="Logo" width="90" height="90">

<h3 align="center">Python Skill Project</h3>
</div>

## Prerequisites
Before you begin, ensure you have the following installed:
 
* [![Python][Python]][Python-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![Celery][Celery]][Celery-url]
* [![Redis][redis]][Redis-url]
* [![ElasticSearch][elasticsearch]][ElasticSearch-url]
* [![Nginx][nginx]][nginx-url]

## Table of Contents

1. [Installation](#installation)
    - [Python](#python)
2. [Project Overview](#project-overview)
    - [Project Structure](#project-structure)
    - [Celery](#celery)
    - [ElasticSearch](#elasticSearch)
    - [Deployment in Python](#deployment-in-python)

## Installation

### Python

To run this project, you need to have Python installed. If you haven't installed Python yet, you can download it from the [official Python website](https://www.python.org/downloads/).

### Project Structure.
```
python_skills
├─ celery_app
│  ├─ img
│  │  ├─ celery_diagram.png
│  │  └─ celery_logo.png
│  └─ README.md
├─ deployment_app
│  ├─ nginx.png
│  └─ README.md
├─ elastic_search_app
│  └─ README.md
├─ python_logo.png
└─ README.md

```

## Project Overview
Provide an overview of the project and explain the components being used.

### Celery
- Celery is a distributed task queue that is used to handle asynchronous tasks in this project. It allows you to run tasks in the background, making your application more responsive.

- To install Celery, you can use pip:
    ```
    pip install celery
    ```

### ElasticSearch
- OpenSearch is a distributed search and analytics engine. It is being utilized in this project for [specific functionality].
- To install opensearch, you can use pip:
    ```
    pip install opensearch-py
    ```

### Deployment in Python
- Deployment in Python can be facilitated through various methods and tools, including Docker, Kubernetes, or traditional server setups. However, in this project, we recommend utilizing Nginx for reverse proxying and serving static files, coupled with a service file for managing the Python application.


<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=Blue
[Python-url]: https://docs.python.org/3.10/
[FastAPI]: https://img.shields.io/badge/FastAPI-20232A?style=for-the-badge&logo=fastapi&logoColor=009485
[FastAPI-url]: https://fastapi.tiangolo.com/
[Celery]: https://img.shields.io/badge/celery-008000?style=for-the-badge&logo=celery&logoColor=Blue
[Celery-url]: https://docs.celeryq.dev/en/stable/
[Redis]: https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/docs/about/
[ElasticSearch]: https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch
[elasticsearch-url]: https://www.elastic.co/
[Nginx]: https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white
[Nginx-url]: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-go-web-application-using-nginx-on-ubuntu-18-04
