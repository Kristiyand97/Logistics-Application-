from core.command_factory import CommandFactory
from core.engine import Engine
from core.logistics import Logistics

logistics = Logistics()
cmd_factory = CommandFactory(logistics)
engine = Engine(cmd_factory)

engine.start()
