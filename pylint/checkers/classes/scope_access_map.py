# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/main/LICENSE


import collections

from pylint.checkers.utils import node_frame_class


def _scope_default():
    return collections.defaultdict(list)


class ScopeAccessMap:
    """Store the accessed variables per scope."""

    def __init__(self):
        self._scopes = collections.defaultdict(_scope_default)

    def set_accessed(self, node):
        """Set the given node as accessed."""

        frame = node_frame_class(node)
        if frame is None:
            # The node does not live in a class.
            return
        self._scopes[frame][node.attrname].append(node)

    def accessed(self, scope):
        """Get the accessed variables for the given scope."""
        return self._scopes.get(scope, {})
