from commands.create_package import CreatePackageCommand
from commands.create_route import CreateRouteCommand
from commands.search_route import SearchRouteCommand
from core.logistics import Logistics
from core.models_factory import ModelsFactory


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
        # if cmd.lower() == "addtestrun":
        #     return AddTestRunCommand(params, self.logistics, self._models_factory)
        # if cmd.lower() == "testreport":
        #     return TestReportCommand(params, self.logistics)
        # if cmd.lower() == "viewgroup":
        #     return ViewGroupCommand(params, self.logistics)
        # if cmd.lower() == "viewsystem":
        #     return ViewSystemCommand(params, self.logistics)

        raise ValueError(f'Invalid command name: {cmd}!')
