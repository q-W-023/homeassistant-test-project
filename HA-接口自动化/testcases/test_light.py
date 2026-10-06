from common.assert_utils import ApiAssert


class TestLight:
    ENTITY = "light.bed_light"

    def test_turn_on_and_read_back(self, api):
        resp = api.post("/api/services/light/turn_on", json={"entity_id": self.ENTITY})
        ApiAssert.status(resp, 200)
        state = api.get(f"/api/states/{self.ENTITY}").json()
        assert state["state"] == "on"

    def test_turn_off_and_read_back(self, api):
        resp = api.post("/api/services/light/turn_off", json={"entity_id": self.ENTITY})
        ApiAssert.status(resp, 200)
        state = api.get(f"/api/states/{self.ENTITY}").json()
        assert state["state"] == "off"

    def test_invalid_service(self, api):
        resp = api.post("/api/services/foo/bar", json={})
        ApiAssert.status(resp, 400)
