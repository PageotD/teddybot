FROM debian:stable
RUN apt-get -y update
RUN apt-get -y install git python3 python3-pip python3-virtualenv
RUN pip3 install discord.py pyyaml python-dotenv
COPY . /home/app
WORKDIR "/home/app"
CMD [ "python3", "/home/app/teddybot.py" ]