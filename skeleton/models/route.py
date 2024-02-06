class Route:
    id = 1

    def __init__(self, locations: list[list]):
        self.locations = locations
        self.packages = []
        self.route_id = Route.id
        Route.id += 1





