FROM python:3.11.0b1-slim-buster

WORKDIR /service

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]