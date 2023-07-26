FROM python:3.11

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR tracking

EXPOSE 8000

#CMD ["python", "manage.py", "runserver"]
#
#RUN cd bot

#CMD ["python", "app.py"]
