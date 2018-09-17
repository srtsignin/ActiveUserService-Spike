FROM python:3.6-alpine3.6

WORKDIR /runner

ADD requirements.txt /runner
RUN pip install -r requirements.txt

ADD active_user_service.py /runner

EXPOSE 65001

CMD python active_user_service.py