FROM python:3.13-bullseye

WORKDIR /app_gfc

ENV MPLBACKEND=agg

RUN apt-get update -y

RUN apt-get upgrade -y

RUN apt-get install -y libx11-dev

RUN apt-get install -y python3-tk

RUN apt-get install -y python3-matplotlib

RUN pip install --upgrade pip

RUN python -m venv .venv

RUN . .venv/bin/activate

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /app/ .

COPY gunicorn_config.py .

COPY gfc_linux.cfg gfc.cfg

EXPOSE 8080

CMD ["gunicorn","--config", "gunicorn_config.py", "main:app"]
