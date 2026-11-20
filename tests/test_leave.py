from leavetracker.main import app


def test_health():
    assert app.test_client().get("/health").get_json() == {"status": "ok"}


def test_balance():
    r = app.test_client().get("/leave/e1")
    assert r.status_code == 200
    assert r.get_json()["remaining"] == 15


def test_unknown_employee():
    assert app.test_client().get("/leave/zzz").status_code == 404