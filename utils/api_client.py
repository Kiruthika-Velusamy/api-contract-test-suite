import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:

    def __init__(self,base_url:str):
        self.base_url=base_url
        self.session=requests.session();
        self.session.headers.update({"Content-Type":"application/json","Accept":"application/json"})

    def set_auth_token(self,auth_token:str):
        self.session.headers.update({"Cookie":f"token={auth_token}"})
        logger.info("Auth token set")

    def get(self,endpoint:str, **kwargs):
        url=f"{self.base_url}{endpoint}"
        logger.info(f"Get {url}")
        response=self.session.get(url,**kwargs)
        logger.info(f"Response: {response.status_code}")
        return response

    def post(self,endpoint:str, **kwargs):
        url=f"{self.base_url}{endpoint}"
        logger.info(f"Get {url}")
        response=self.session.post(url,**kwargs)
        logger.info(f"Response: {response.status_code}")
        return response