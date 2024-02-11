from skeleton.core.logistics import Logistics


class BaseCommand():
    def __init__(self, params: list[str], logistics: Logistics):
        self._params = params
        self._logistics = logistics

    @property
    def params(self):
        return tuple(self._params)

    @property
    def app_data(self):
        return self._app_data

    def execute(self):
        # override in derived classes
        return ""
