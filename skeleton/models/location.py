class Location:
    def __init__(self, name: str, routes: list[list], packages: list[list]):
        self.name = name
        self.routes = routes
        self.packages = packages

    def add_route(self, route):
        pass

    def receive_package(self, package):
        pass

    def dispatch_package(self, package):
        pass

    def get_hub_status(self):
        pass
