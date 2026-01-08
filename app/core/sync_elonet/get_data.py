from core.request_bot import RequestBot
from requests import RequestException
from utils.logger import logger


class GetData:
    req = RequestBot(url="https://service.elonethabitacao.com.br/SIAR/api")
    token = None

    def __login__(self):
        body = {
            "codigoAcesso": "1901",
            "usuario": "Renato",
            "senha": "#Renatoapi25"
        }
        response = self.req.post(path="auth/login", body=body)
        return response

    def getToken(self):
        if self.token is None:
            response = self.__login__()
            self.token = response['data']['token']
        return self.token

    def getEntitys(self, path: str):
        pag = {
            "page": 1,
            "per-page": 100,
            "has_next_page": True
        }

        try:
            nHeaders = {
                "Authorization": f"Bearer {self.getToken()}",
            }
            process = 1
            while pag['has_next_page']:
                resp = self.req.get(
                    path=f"{path}?page={pag['page']}&per-page={pag['per-page']}",
                    nHeaders=nHeaders
                )
                for item in resp['data']:
                    yield {"processing": process, "total": resp['pagination']['total'], "data": item}
                    process += 1
                pag['page'] = resp['pagination']['next_page']
                pag['has_next_page'] = resp['pagination']['has_next_page']

        except RequestException as exp:
            if exp.response is not None and exp.response.status_code == 401:
                self.token = None
                self.getToken()
                return self.getEntitys(path)
            else:
                logger.exception('Erro ao obter os dados: %s', exp)
                raise exp
        except Exception as e:
            logger.exception('Erro ao obter os dados: %s', e)
            raise e
