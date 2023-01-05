FROM python:3.10-slim-bullseye

WORKDIR /backend

COPY requirements.txt ./requirements.txt

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY backend/src ./src

CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0", "--port", "8000"]
