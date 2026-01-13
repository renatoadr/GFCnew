FROM python:3.13-bullseye

WORKDIR /app_gfc

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

COPY pyproject.toml .

COPY gfc_linux.cfg gfc.cfg

EXPOSE 5000

CMD ["waitress-serve","--listen=*:5000", "main:app"]
