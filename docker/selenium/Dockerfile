FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    default-jre \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Allure CLI
RUN wget -q https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -zxf allure-2.27.0.tgz \
    && mv allure-2.27.0 /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/local/bin/allure \
    && rm allure-2.27.0.tgz

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /tests

COPY app/tests/requirements.txt .
RUN pip install -r requirements.txt

COPY app/tests/e2e_tests.py .

CMD ["sh", "-c", "python3 e2e_tests.py; allure generate /tmp/allure-results -o /tmp/allure-report --clean; echo 'Allure report generated at /tmp/allure-report'"]
