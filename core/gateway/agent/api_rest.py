import requests

from gateway.router import Agent


class APIRestAgent(Agent):
    def process(self, url, method, payload={}, data="", headers={}, **kwargs):
        return requests.request(
            method=method,
            url=url,
            params=payload,
            data=data,
            headers=headers
        ).content.decode('utf-8')

