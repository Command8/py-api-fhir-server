
#from http import server
from urllib import response
import smtplib
import get_fhir
import unittest
from unittest.mock import patch
import MockData


class TestGetFhir (unittest.TestCase):
    def test_request(self):
        fake_json = [{'Soumil':"Python"}]
        with patch('MockData.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = Gold()
            response = obj.get
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),obj.get.json)

    if __name__ == '__main__':
        unittest.main()

          



