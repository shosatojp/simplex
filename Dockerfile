FROM ubuntu:latest

# RUN apk add wget
RUN apt-get update && apt-get -y install wget python3
RUN wget https://github.com/yudai/gotty/releases/download/v1.0.1/gotty_linux_amd64.tar.gz -O gotty.tar.gz
RUN tar xfv gotty.tar.gz
RUN apt-get -y install python3-pip
RUN python3 -m pip install numpy sympy pandas
COPY ./simplex/simplex.py .
CMD /gotty -p 8080 python3 stdin.py