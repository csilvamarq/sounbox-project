#Deriving the latest base image
FROM python:latest

RUN apt-get update -y && apt-get install portaudio19-dev -y
#Labels as key value pair
LABEL Maintainer="Misil4"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /app

COPY ./VoiceBox/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./VoiceBox/voiceBox.py .


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python3","-u", "voiceBox.py"]