from skeleton.models.delivery_route import DeliveryRoute


class AllRoutes:

    def __init__(self):
        self._delivery_routes = {}

    @property
    def delivery_routes(self):
        return tuple(self._delivery_routes.items())

    def create_route(self, route: str, start_time) -> DeliveryRoute:
        if route in self.delivery_routes:
            raise ValueError(f"Delivery route already exists")
        new_route = DeliveryRoute(route, start_time)
        self.delivery_routes[id] = new_route
        return new_route

    def get_route_by_id(self, route_id: int) -> DeliveryRoute:
        route = self.delivery_routes.get(route_id)
        if route is None:
            raise ValueError(f"No route with id: {route_id} exists")
        return route
