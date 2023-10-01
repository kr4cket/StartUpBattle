FROM python:3
WORKDIR /
RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "-u", "main.py"]