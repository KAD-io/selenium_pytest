FROM selenium/standalone-firefox:latest

ENV HEADLESS=1
ENV BROWSER=firefox
RUN sudo apt update && sudo apt upgrade -y
RUN sudo apt install python3-pip -y
RUN python3 -m pip install pytest pytest-cov selenium webdriver-manager
RUN mkdir /home/seluser/test
COPY . /home/seluser/test
WORKDIR /home/seluser/test
RUN sudo chmod -R 757 /home/seluser/test