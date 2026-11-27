from app import is_legacy, ua
def test_legacy(): assert is_legacy("not-a-version")
def test_ua(): assert ua().startswith("python-requests/")
