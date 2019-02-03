import numpy as np


class NodeList(list):

    def __contains__(self, item):
        for node in self:
            if np.array_equal(node.taquin, item.taquin):
                return True
        return False

    def __str__(self):
        ret = "Node List:"
        for node in self:
            ret += " (id:{} ; f:{} ; grid:{})".format(node.id, node.heuristic, "".join(map(str, list(node.taquin.grid))))
        return ret
