class ApiAssert:
    @staticmethod
    def status(resp, expected):
        assert resp.status_code == expected, \
            f"状态码不符：期望 {expected}，实际 {resp.status_code}，响应={resp.text}"

    @staticmethod
    def json_value(resp, dotted_path, expected):
        value = resp.json()
        for key in dotted_path.split("."):
            value = value[key]
        assert value == expected, f"字段 {dotted_path} 期望 {expected}，实际 {value}"
