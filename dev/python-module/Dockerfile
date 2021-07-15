FROM python:3.7-slim-buster

WORKDIR /app

COPY pip-packages.txt ./

RUN apt-get update && apt-get install -y wget firefox-esr
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.28.0-linux64.tar.gz
RUN chmod +x geckodriver

ENV PATH="/app:${PATH}"

RUN pip install -r pip-packages.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
