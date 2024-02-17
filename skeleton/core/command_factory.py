from skeleton.commands.assign_package import AssignPackage
from skeleton.commands.create_package import CreatePackageCommand
from skeleton.commands.create_route import CreateRouteCommand
from skeleton.commands.search_route import SearchRouteCommand
from skeleton.commands.view_route import ViewRouteCommand
from skeleton.commands.view_truck import ViewTruckCommand
from skeleton.commands.view_unassigned_packages import ViewUnassignedPackagesCommand
from skeleton.core.logistics import Logistics
from skeleton.core.models_factory import ModelsFactory
from skeleton.commands.view_package import ViewPackageCommand
from skeleton.commands.assign_route import AssignRouteToTruck



class CommandFactory:
    def __init__(self, logistics: Logistics):
        self.logistics = logistics
        self._models_factory = ModelsFactory()

    def create(self, input_line: str):
        cmd, *params = input_line.split()

        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self.logistics, self._models_factory)
        if cmd.lower() == "createpackage":
            return CreatePackageCommand(params, self.logistics, self._models_factory)
        if cmd.lower() == "searchroute":
            return SearchRouteCommand(params, self.logistics,self._models_factory)
        if cmd.lower() == "viewpackage":
            return ViewPackageCommand(params, self.logistics,self._models_factory)
        if cmd.lower() == "assignroute":
            return AssignRouteToTruck(params, self.logistics,self._models_factory)
        if cmd.lower() == "assignpackage":
            return AssignPackage(params, self.logistics,self._models_factory)
        if cmd.lower() == "viewtruck":
            return ViewTruckCommand(params, self.logistics, self._models_factory)
        if cmd.lower() == "viewroute":
            return ViewRouteCommand(params, self.logistics, self._models_factory)
        if cmd.lower() == "viewunassignedpackages":
            return ViewUnassignedPackagesCommand(params, self.logistics, self._models_factory)
        raise ValueError(f'Invalid command name: {cmd}!')
