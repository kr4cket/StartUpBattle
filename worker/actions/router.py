import json
from worker.actions.service import Service


class Router:

    def __init__(self):
        self.service = Service()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Router, cls).__new__(cls)
        return cls.instance

    def run(self, data: json):
        json_data = json.loads(data)
        method_name = json_data.pop("type")
        getattr(self.service, method_name)(json_data)
