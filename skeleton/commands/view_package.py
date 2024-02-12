from commands.base_command import BaseCommand
from core.logistics import Logistics
from core.models_factory import ModelsFactory


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
        package_id = self.params[0]






        start_location = self.params[0]
        end_location = self.params[1]
        weight = self.params[2]
        contact_info = self.params[3]
        new_package = self.models_factory.create_package(start_location,end_location,weight,contact_info)

        self.logistics.add_package(new_package)

        return f'Package #{package_id} created'
