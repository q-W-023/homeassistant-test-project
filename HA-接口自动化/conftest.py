
import pytest
from common.client import HttpClient

@pytest.fixture(scope="session")
def api():
    return HttpClient()

@pytest.fixture(scope="session")
def wrong_token_api():
    return HttpClient(token="wrong")        # 错误令牌

@pytest.fixture(scope="session")
def empty_token_api():
    return HttpClient(token="")             # 空令牌

@pytest.fixture(scope="session")
def no_auth_api():
    return HttpClient(use_auth=False)       # 完全不带认证头
