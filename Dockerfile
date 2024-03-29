FROM python:3.11-slim-bullseye

WORKDIR /app

COPY src/requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/ /app

ARG APP_VERSION
ENV APP_VERSION="$APP_VERSION"

ENTRYPOINT ["python3"]
CMD ["app.py"]
