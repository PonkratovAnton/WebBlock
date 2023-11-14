FROM python:3

WORKDIR /app

COPY requirements.txt .
COPY app/create_db.py /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONPATH="/app:${PYTHONPATH}"

CMD ["sh", "-c", "sleep 30 && python create_db.py && python runner.py"]
