FROM python:3.10-slim
WORKDIR /

COPY . ./

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "main.py"]