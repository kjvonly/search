FROM ubuntu:latest

RUN DEBIAN_FRONTEND=noninteractive apt update && apt upgrade -y && apt install -y curl python3 gzip

WORKDIR /usr/src/app/

# copy the files we need
COPY mapping.json .
COPY parse.py .
COPY seed.sh .
RUN chmod 744 seed.sh

ENTRYPOINT ["./seed.sh"]