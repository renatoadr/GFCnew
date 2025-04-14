FROM python:3.11

WORKDIR /app_gfc

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
