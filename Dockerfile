FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update -q; \
	apt-get install -y --no-install-recommends \
		cmake \
		pkg-config \
		libx11-dev \
		libatlas-base-dev \
		libgtk-3-dev \
		libboost-python-dev \
	&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=7000                             \
    ALLOWED_HOSTS=localhost               \
    PREFIX_URL=