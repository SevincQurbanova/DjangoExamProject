FROM python:3.12

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install celery  # Install Celery

# Copy project files
COPY . /app/
