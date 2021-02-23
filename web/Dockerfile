FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./web /code
RUN pip install -r requirements.txt && \
  mv /code/entrypoint /entrypoint && \
  chmod +x /entrypoint && \
  mv /code/start /start && \
  chmod +x /start


ENTRYPOINT ["/entrypoint"]