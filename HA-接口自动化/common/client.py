import requests
from common.config_loader import config
from common.logger import logger

class HttpClient:
    def __init__(self, base_url=None, token=None, timeout=None, use_auth=True):
        self.base_url = (base_url or config.base_url).rstrip("/")
        self.timeout = timeout or config.timeout
        self.session = requests.Session()
        self.session.headers["Content-Type"] = "application/json"
        if use_auth:
            self.session.headers["Authorization"] = f"Bearer {config.token if token is None else token}"

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        kwargs.setdefault("timeout", self.timeout)
        logger.info(f"→ {method} {url} json={kwargs.get('json')}")
        resp = self.session.request(method, url, **kwargs)
        logger.info(f"← {resp.status_code} {resp.text[:300]}")
        return resp

    def get(self, path, **kwargs):  return self.request("GET", path, **kwargs)
    def post(self, path, **kwargs): return self.request("POST", path, **kwargs)
