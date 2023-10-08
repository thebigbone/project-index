FROM python:3-alpine

RUN apk update && apk upgrade && apk add --no-cache git

RUN git clone https://github.com/thebigbone/project-index.git

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt    

EXPOSE 5000

CMD ["flask", "run"]