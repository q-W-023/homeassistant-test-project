import pytest
from common.assert_utils import ApiAssert

@pytest.fixture()
def fresh_add_on(api):
    """确保 update.demo_add_on 处于初始版本；否则跳过（该用例天然不可重复执行）"""
    ver = api.get("/api/states/update.demo_add_on").json()["attributes"]["installed_version"]
    if ver != "1.0.0":
        pytest.skip(f"update.demo_add_on 当前已是 {ver}（被上次运行升级过），"
                    f"需重启 HA 复位后才能重跑")

@pytest.mark.slow
class TestUpdate:
    def test_add_on_update_flow(self, api,fresh_add_on):
        st = api.get("/api/states/update.demo_add_on").json()
        assert st["attributes"]["installed_version"] == "1.0.0"
        ApiAssert.status(api.post("/api/services/update/install",
                                  json={"entity_id": "update.demo_add_on"}), 200)
        st = api.get("/api/states/update.demo_add_on").json()
        assert st["attributes"]["installed_version"] == "1.0.1"
        assert st["state"] == "off"

    @pytest.mark.parametrize("entity, code", [
        ("update.demo_update_no_install", 500),
        ("update.not_exist", 200),
    ])
    def test_install_various(self, api, entity, code):
        resp = api.post("/api/services/update/install", json={"entity_id": entity})
        ApiAssert.status(resp, code)

    def test_install_empty_body(self, api):
        ApiAssert.status(api.post("/api/services/update/install", json={}), 400)

    def test_install_malformed_json(self, api):
        resp = api.post("/api/services/update/install",
                        data='{"entity_id":',
                        headers={"Content-Type": "application/json"})
        ApiAssert.status(resp, 400)
