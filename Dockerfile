FROM python:3.10-slim-bullseye

WORKDIR /forum

COPY requirements.txt ./requirements.txt

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./forum-app ./forum-app

CMD ["python", "/forum/forum-app/manage.py", "runserver"]
