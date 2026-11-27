import requests, six
from packaging.version import parse, LegacyVersion  # LegacyVersion removed in packaging 22

def is_legacy(v):
    return isinstance(parse(v), LegacyVersion)

def ua():
    return requests.utils.default_user_agent()
