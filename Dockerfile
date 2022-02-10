FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install -r requirements
CMD flask run --host=0.0.0.0