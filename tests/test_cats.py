import requests
from pytest_voluptuous import S
from voluptuous import Schema, Any, ALLOW_EXTRA

from schemas.facts import facts
from utils.sessions import cats


def test_facts_count():
    limit = 2
    response = requests.get("https://catfact.ninja/facts", params={'limit': limit})
    assert len(response.json()['data']) == limit


def test_facts_count_v2():
    limit = 2
    response = cats().get("/facts", params={"limit": limit})
    assert len(response.json()['data']) == limit


def test_fact_schema_validation():
    limit = 2
    schema = Schema({
        'current_page': int,
        'data': [
            {
                'fact': str,
                'length': int
            }
        ],
        'first_page_url': str,
        'from': int,
        'last_page': int,
        'last_page_url': str,
        'links': [
            {
                'url': Any(None, str),
                'label': str,
                'active': bool
            }
        ],
        'next_page_url': str,
        'path': str,
        'per_page': str,
        'prev_page_url': Any(None, str),
        'to': int,
        'total': int
    })

    response = requests.get("https://catfact.ninja/facts", params={'limit': limit})

    assert S(schema) == response.json()
    assert response.status_code == 200


def test_fact_schema_validation_short():
    limit = 2

    response = requests.get("https://catfact.ninja/facts", params={'limit': limit})

    assert S(facts) == response.json()
    assert response.status_code == 200
