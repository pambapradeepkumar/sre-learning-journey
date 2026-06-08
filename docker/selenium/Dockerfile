FROM python:3.11-slim

USER root

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /tests

COPY app/tests/requirements.txt .
RUN pip install -r requirements.txt

COPY app/tests/e2e_tests.py .

CMD ["python3", "e2e_tests.py"]
