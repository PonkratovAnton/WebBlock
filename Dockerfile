FROM python:3

WORKDIR /app

COPY requirements.txt .
COPY app/create_db.py /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONPATH="/app:${PYTHONPATH}"

CMD ["sh", "-c", "sleep 10 && python runner.py && python create_db.py"]
