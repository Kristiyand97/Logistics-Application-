from skeleton.commands.base_command import BaseCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory



class ViewUnassignedPackagesCommand(BaseCommand):
    def __init__(self, params: list[str],
                 logistics: Logistics,
                 models_factory: ModelsFactory):
        super().__init__(params, logistics)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        unassigned_packages = "Unassigned Packages ID: "
        for package in self.logistics.packages:
            if package.assigned_route is None:
                unassigned_packages += f"\n{package.package_id}"
        return unassigned_packages


