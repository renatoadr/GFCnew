import requests
import json

from utils.logger import logger


class RequestBot:
    session = requests.Session()

    headers = {
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'referer': "https://gfcpro.com.br",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    def __init__(self, url: str):
        self.url = url

    def __request__(self, path, nHeaders: dict = None, body: dict = None):
        logger.info('Preparando para enviar a solicitação...')

        self.session.headers.update(self.headers)

        if nHeaders is not None:
            self.session.headers.update(nHeaders)

        logger.info(
            'Enviando a solicitação para a URL: %s',
            self.url + '/' + path
        )

        if body is not None:
            response = self.session.post(
                f"{self.url}/{path}",
                timeout=60,
                allow_redirects=True,
                json=body,
                verify=False
            )
        else:
            response = self.session.get(
                f"{self.url}/{path}",
                timeout=60,
                allow_redirects=False,
                verify=False
            )
        logger.info('Solicitação enviada. Código de status: %s',
                    response.status_code)
        response.raise_for_status()
        if response.headers.get('Content-Type', '').startswith('application/json'):
            return json.loads(response.content)
        return response.content

    def get(self, path, nHeaders: dict = None):
        try:
            return self.__request__(path, nHeaders)
        except requests.exceptions.RequestException as e:
            logger.exception('Erro ao fazer a solicitação GET: %s', e)
            raise

    def post(self, path, body: dict, nHeaders: dict = None):
        try:
            return self.__request__(path, nHeaders, body)
        except requests.exceptions.RequestException as e:
            logger.exception('Erro ao fazer a solicitação POST: %s', e)
            raise
