#Deriving the latest base image
FROM python:3.8-buster


#Labels as key value pair
LABEL Maintainer="Misil4"

RUN apt-get update -y && apt-get install portaudio19-dev -y
# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /app
RUN apt-get update && apt-get install git -y
RUN pip3 install setuptools-rust
RUN pip3 install git+https://github.com/openai/whisper.git
RUN apt-get install -y ffmpeg

COPY ./Transcribe/transcriber.py .
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python3","-u", "transcriber.py"]