# syntax=docker/dockerfile:1.3-labs
FROM python:3.10.4

ARG UID=1000
ARG GID=1000

RUN apt-get -qq update && \
    apt-get -qqy install sudo curl netcat && \
    rm -rf /var/lib/apt/lists/

RUN groupadd -g "${GID}" watchmate \
    && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" watchmate

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    adduser --disabled-password --gecos "" watchmate && \
    adduser watchmate sudo

USER watchmate
WORKDIR /home/watchmate

RUN mkdir /home/watchmate/database
RUN mkdir /home/watchmate/code
WORKDIR /home/watchmate/code

ENV PYTHONUNBUFFERED 1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/home/watchmate/.local/bin

COPY --chown=watchmate pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY --chown=watchmate ./ ./

ENTRYPOINT [ "./entrypoint.sh" ]