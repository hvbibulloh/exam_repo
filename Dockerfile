FROM python:3.11-alpine
LABEL authors="hvbibulloh"

WORKDIR /apps
COPY . /apps

ENV TOKEN=my_value
RUN pip install -r req.txt

ENTRYPOINT ["python", "exam.py"]