from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory


class AssignPackage(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        # TODO Add validation for param
        package_id = int(self.params[0])

        return self.logistics.assign_package_to_optimal_route(package_id)
