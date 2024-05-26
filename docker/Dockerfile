FROM python:3.12
WORKDIR /docker
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /docker
CMD ["python", "main.py"]