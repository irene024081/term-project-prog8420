# syntax=docker/dockerfile:1.3-labs
FROM python:3.10.4

RUN apt-get -qq update && \
    apt-get -qqy install sudo curl netcat && \
    rm -rf /var/lib/apt/lists/

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    adduser --disabled-password --gecos "" watchmate && \
    adduser watchmate sudo

USER watchmate
WORKDIR /home/watchmate

RUN mkdir -p /opt/watchmate

ENV PYTHONUNBUFFERED 1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/home/watchmate/.local/bin

COPY --chown=watchmate pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY --chown=watchmate ./ ./

ENTRYPOINT [ "./entrypoint.sh" ]