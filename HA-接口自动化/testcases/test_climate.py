from common.assert_utils import ApiAssert


class TestClimate:
    ENTITY = "climate.ecobee"

    def test_set_hvac_mode(self, api):
        resp = api.post("/api/services/climate/set_hvac_mode",
                        json={"entity_id": self.ENTITY, "hvac_mode": "heat_cool"})
        ApiAssert.status(resp, 200)

    def test_set_temperature_and_read_back(self, api):
        resp = api.post("/api/services/climate/set_temperature",
                        json={"entity_id": self.ENTITY,
                              "target_temp_high": 77, "target_temp_low": 68})
        ApiAssert.status(resp, 200)
        back = api.get(f"/api/states/{self.ENTITY}")
        ApiAssert.json_value(back, "attributes.target_temp_high", 77)

    def test_temperature_param_mismatch(self, api):
        resp = api.post("/api/services/climate/set_temperature",
                        json={"entity_id": self.ENTITY, "temperature": 22})
        ApiAssert.status(resp, 500)
