FROM python:slim-buster
RUN pip3 install discord.py pyyaml python-dotenv emoji
COPY . /app
CMD [ "python3", "/app/teddybot.py" ]