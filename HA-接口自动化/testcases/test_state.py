from common.assert_utils import ApiAssert


class TestStates:
    def test_list_states(self, api):
        resp = api.get("/api/states")
        ApiAssert.status(resp, 200)
        assert isinstance(resp.json(), list) and len(resp.json()) > 0

    def test_single_state(self, api):
        resp = api.get("/api/states/light.bed_light")
        ApiAssert.json_value(resp, "entity_id", "light.bed_light")

    def test_not_exist_entity(self, api):
        ApiAssert.status(api.get("/api/states/light.not_exist"), 404)
