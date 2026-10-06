from common.assert_utils import ApiAssert


class TestConfig:
    def test_get_config(self, api):
        ApiAssert.status(api.get("/api/config"), 200)

    def test_discovery_info_404(self, api):
        ApiAssert.status(api.get("/api/discovery_info"), 404)
