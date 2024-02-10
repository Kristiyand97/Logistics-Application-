from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory


class CreatePackageCommand(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        # TODO Add validation for params
        start_location = self.params[0]
        end_location = self.params[1]
        weight = self.params[2]
        contact_info = self.params[3]
        new_package = self.models_factory.create_package(start_location,end_location,weight,contact_info)

        self.logistics.add_package(new_package)

        return f'Package #{new_package.package_id} created'
