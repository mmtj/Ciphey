from typing import Set, Optional, Dict

from .ausearch import Node, AuSearch
from ciphey.iface import (
    Config,
    registry,
    ParamSpec,
)


@registry.register
class Perfection(AuSearch):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def findBestNode(self, nodes: Set[Node]) -> Node:
        return next(iter(nodes))

    def __init__(self, config: Config):
        super().__init__(config)
