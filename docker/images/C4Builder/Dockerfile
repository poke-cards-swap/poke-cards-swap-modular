FROM openjdk:16-slim

ENV PUPPETEER_SKIP_DOWNLOAD 1

RUN apt update && apt install -y graphviz nodejs npm

RUN npm install -g c4builder

EXPOSE 3000

ENTRYPOINT ["c4builder"]
