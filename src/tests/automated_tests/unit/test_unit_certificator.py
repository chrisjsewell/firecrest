import pytest
import requests
import os
from markers import host_environment_test

FIRECREST_IP = os.environ.get("FIRECREST_IP")
if FIRECREST_IP:
	CERTIFICATOR_URL = os.environ.get("FIRECREST_IP") + "/certificator"
else:
    CERTIFICATOR_URL = os.environ.get("CERTIFICATOR_URL")	




# Test get a certificate
@host_environment_test
def test_receive(headers):
	url = "{}/".format(CERTIFICATOR_URL)
	resp = requests.get(url, headers=headers)
	print(resp.content)
	assert resp.status_code == 200  


# Test get status of certificator microservice
@host_environment_test
def test_status(headers):
	url = "{}/status".format(CERTIFICATOR_URL)
	resp = requests.get(url, headers=headers)
	print(resp.content)
	assert resp.status_code == 200


if __name__ == '__main__':
	pytest.main()
