from skeleton.core.command_factory import CommandFactory
from skeleton.core.engine import Engine
from skeleton.core.logistics import Logistics

logistics = Logistics()
cmd_factory = CommandFactory(logistics)
engine = Engine(cmd_factory)

engine.start()
