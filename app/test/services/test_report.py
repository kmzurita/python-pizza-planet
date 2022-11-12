import pytest
from app.utils.functions import OK_STATUS


def test_get_report_service_returns_three_reports_when_calls_get_method(client, report_uri):
    response = client.get(f'{report_uri}')
    pytest.assume(response.status.startswith(OK_STATUS))
