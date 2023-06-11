FROM python:3.9.17-bullseye

WORKDIR /etc/opt/site/

COPY . .

RUN pip install poetry==1.5.0
RUN poetry install --with production

ENTRYPOINT ["bash", "entrypoint.sh"]