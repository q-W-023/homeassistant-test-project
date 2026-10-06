from common.assert_utils import ApiAssert

class TestHealth:
    def test_health_check(self, api):
        resp = api.get("/api/")
        ApiAssert.status(resp, 200)
        assert resp.json()["message"] == "API running."
