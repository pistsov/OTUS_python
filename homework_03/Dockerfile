#to launch the app please run the following command in terminal: docker run -p 8000:8000 -it app

FROM python:3.11.4-slim-bookworm

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --only main

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000