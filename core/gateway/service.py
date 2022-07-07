import os
import json
from typing import List, Union
from io import IOBase

from .router import Router, Route, Middleware, Agent
from .exceptions import ConfigNotDefinedAtConfigFile
from .agent.api_rest import APIRestAgent


class RouteDefinition:
    def __init__(self, route, endpoint):
        self.route = route
        self.endpoint = endpoint


class RouteTableService:
    def __init__(self):
        self.table: List[RouteDefinition] = []

    def load(self, route_file: Union[str, IOBase]) -> None:
        """Loads routes configurations to memory.

        :param route_file: A json file that contains information related
            to routes.
                - If str parameter, pass the path of the file
                - if IOBase, pass a file that follow the json protocol
        :return: None
        """
        if isinstance(route_file, str):
            routes = json.loads(open(route_file).read())
        else:
            routes = json.loads(route_file.read())

        for route in routes:
            try:
                url = route['url']
                method = route['method']
                headers = route['headers']
                endpoint = route['gateway_endpoint']
                agent = APIRestAgent()
                middlewares = []
            except KeyError as e:
                raise ConfigNotDefinedAtConfigFile(str(e))

            route_object = Route(
                url=url,
                method=method,
                headers=headers,
                agent=agent,
                middlewares=middlewares
            )
            route_definition = RouteDefinition(
                route=route_object,
                endpoint=endpoint
            )
            self.table.append(route_definition)


class RouterRequisitionService:
    @staticmethod
    def route(route: Route
              , params: Union[dict, None] = None
              , body: Union[str, bytes, dict, List[tuple], None] = None) -> str:

        router = Router()
        response = router.route(
            route=route,
            payload=params,
            body=body
        )

        return response
