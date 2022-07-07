import requests
from typing import List, Union, Callable
from abc import ABC


class Agent(ABC):
    def process(self, **kwargs) -> str:
        pass


class Middleware(ABC):
    @staticmethod
    def process() -> dict:
        pass


class Route:
    def __init__(self, url: str, method: str, headers: dict, agent: Agent, middlewares: List[Middleware]):
        self.url = url
        self.method = method
        self.headers = headers
        self.agent = agent
        self.middlewares = middlewares

    def process(self, **kwargs):
        args = self.__dict__
        args.update(kwargs)
        return self.agent.process(**args)


class Router:

    @staticmethod
    def route(route: Route, **kwargs) -> str:

        middleware_args = {}
        for middleware in route.middlewares:
            middleware_args.update(middleware.process())

        response = route.process(**kwargs, **middleware_args)

        return response


