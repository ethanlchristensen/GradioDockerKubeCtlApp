FROM python:3.10-slim

WORKDIR /code

RUN python3 -m venv  ./opt/venv

COPY ./requirements.txt .

RUN . opt/venv/bin/activate

RUN pip install -r ./requirements.txt

COPY . .

CMD ["python", "server.py"]
