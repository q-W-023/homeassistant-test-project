from common.assert_utils import ApiAssert
from common.wait_utils import wait_until


class TestCover:
    ENTITY = "cover.living_room_window"

    def test_open_and_read_back(self, api):
        api.post("/api/services/cover/close_cover", json={"entity_id": self.ENTITY})
        resp = api.post("/api/services/cover/open_cover", json={"entity_id": self.ENTITY})
        ApiAssert.status(resp, 200)
        wait_until(lambda: api.get(f"/api/states/{self.ENTITY}").json()["state"],
                   "opening", timeout=10)

    def test_set_position_and_read_back(self, api):
        resp = api.post("/api/services/cover/set_cover_position",
                        json={"entity_id": self.ENTITY, "position": 50})
        ApiAssert.status(resp, 200)
        wait_until(lambda: api.get(f"/api/states/{self.ENTITY}").json()
                   ["attributes"]["current_position"], 50, timeout=10)

    def test_close_cover(self, api):
        resp = api.post("/api/services/cover/close_cover", json={"entity_id": self.ENTITY})
        ApiAssert.status(resp, 200)
