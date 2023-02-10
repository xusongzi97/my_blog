FROM python:3.9.5

RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip

RUN pip install flask

COPY . /code/

EXPOSE 5000

CMD ["python", "app.py", "runserver", "0.0.0.0:5000"]
