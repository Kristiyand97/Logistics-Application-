from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory


class ViewPackageCommand(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        package_id = int(self.params[0])
        package = self.logistics.get_package_by_id(package_id)

        if package:
            delivery_time_msg = "This package has not yet been assigned to a route" if package.assigned_route is None \
                else f"Delivery time: {self.logistics.calculate_arrival_time(package_id)}"
            return (f"Package ID: {package.package_id}\n"
                    f"End Location: {package.end_location}\n"
                    f"Weight: {package.weight} kg\n"
                    f"Status: {package.status}\n"
                    f"{delivery_time_msg}")
        else:
            return "Package not found."
