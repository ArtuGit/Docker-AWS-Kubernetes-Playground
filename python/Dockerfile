FROM python:3.12.3
WORKDIR /usr/app
COPY . .
COPY .env.docker .env
RUN pip install -r ./requirements.txt
ENTRYPOINT python3 ./src/script.py
