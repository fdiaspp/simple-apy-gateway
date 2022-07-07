from flask import Flask

from ..gateway.service import RouteTableService
from ..gateway.service import RouterRequisitionService


class Api:
    app = Flask(__name__)

    def __init__(self, route_table: RouteTableService):
        self.route_table = route_table

    @app.route("/<endpoint>")
    def main_endpoint(self, endpoint):
        route = self.get_route(endpoint)
        rqs = RouterRequisitionService()
        return rqs.route(route)

    def get_route(self, endpoint):
        return list(
            filter(lambda router_definition: router_definition.endpoint == endpoint
                   , self.route_table.table)
        )[0].route
