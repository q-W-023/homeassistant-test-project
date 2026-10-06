import pytest
from common.assert_utils import ApiAssert


class TestSensor:
    @pytest.mark.parametrize("entity, unit", [
        ("sensor.total_energy_kwh", "kWh"),
        ("sensor.total_gas_m3", "ft³"),
    ])
    def test_sensor_unit(self, api, entity, unit):
        resp = api.get(f"/api/states/{entity}")
        ApiAssert.status(resp, 200)
        ApiAssert.json_value(resp, "attributes.unit_of_measurement", unit)
