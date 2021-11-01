FROM python:3.8.12-slim

WORKDIR /app

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict_with_flask.py", "model.bin", "./"]

EXPOSE 1552

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1552", "predict_with_flask:app"]