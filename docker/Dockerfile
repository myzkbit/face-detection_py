# 3.11.5
FROM python:3   

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
RUN pip install --upgrade pip && pip install dlib

# CMD [ "python", "./your-daemon-or-script.py" ]