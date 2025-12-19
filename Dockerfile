FROM python:3.10-alpine 


COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY src /app
WORKDIR /app
CMD ["python", "app.py"]