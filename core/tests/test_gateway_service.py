import unittest
from io import StringIO
import json

from gateway.service import RouteTableService
from gateway.service import RouterRequisitionService


class RouteTableServiceTest(unittest.TestCase):

    def test_creation(self):
        routes_config = [
            {
                "url": "http://api.vagalume.com.br/search.php",
                "method": "GET",
                "headers": {"Content-Type": "application/json"},
                "gateway_endpoint": "vagalume"
            },
            {
                "url": "http://api.vagalume.com.br/search.php",
                "method": "GET",
                "headers": {"Content-Type": "application/json"},
                "gateway_endpoint": "vagalume_v2"
            }
        ]
        rts = RouteTableService()
        route_file = StringIO(json.dumps(routes_config))

        rts.load(route_file=route_file)
        assert len(rts.table) == 2


class RouterRequisitionServiceTest(unittest.TestCase):

    def test_creation(self):
        routes_config = [
            {
                "url": "http://api.vagalume.com.br/search.php",
                "method": "GET",
                "headers": {"Content-Type": "application/json"},
                "gateway_endpoint": "vagalume"
            },
            {
                "url": "http://api.vagalume.com.br/search.php",
                "method": "GET",
                "headers": {"Content-Type": "application/json"},
                "gateway_endpoint": "vagalume_v2"
            }
        ]
        rts = RouteTableService()
        route_file = StringIO(json.dumps(routes_config))
        rqs = RouterRequisitionService()

        rts.load(route_file=route_file)
        response = rqs.route(route=rts.table[0].route, params={"art": "Madona"})
        response_parsed = json.loads(response)

        assert response_parsed["art"]["name"] == "Madonna"


if __name__ == "__main__":
    unittest.main()
