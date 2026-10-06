from common.assert_utils import ApiAssert


class TestAuth:
    def test_wrong_token(self, wrong_token_api):
        ApiAssert.status(wrong_token_api.get("/api/"), 401)

    def test_empty_token(self, empty_token_api):
        ApiAssert.status(empty_token_api.get("/api/"), 401)

    def test_no_token(self, no_auth_api):
        ApiAssert.status(no_auth_api.get("/api/"), 401)
