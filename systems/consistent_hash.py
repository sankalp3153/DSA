"""
Consistent Hashing Ring with Virtual Nodes.

Used for partitioning Kafka topics, Redis shards, or cache clusters so that
adding/removing a node only remaps ~1/N of keys.

Time Complexity:
  - add_node / remove_node: O(V log(N*V)) where V = virtual nodes per physical node
  - get_node(key): O(log(N*V))
"""

from bisect import bisect_right, insort
import hashlib
from typing import Dict, List, Optional


class ConsistentHashRing:
    def __init__(self, virtual_nodes: int = 128) -> None:
        if virtual_nodes <= 0:
            raise ValueError("virtual_nodes must be positive")
        self.virtual_nodes = virtual_nodes
        self._ring: List[int] = []
        self._node_map: Dict[int, str] = {}
        self._nodes: set[str] = set()

    @staticmethod
    def _hash(key: str) -> int:
        return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)

    def add_node(self, node_id: str) -> None:
        if node_id in self._nodes:
            return
        self._nodes.add(node_id)
        for replica in range(self.virtual_nodes):
            point = self._hash(f"{node_id}#vn{replica}")
            if point not in self._node_map:
                insort(self._ring, point)
                self._node_map[point] = node_id

    def remove_node(self, node_id: str) -> None:
        if node_id not in self._nodes:
            return
        self._nodes.remove(node_id)
        for replica in range(self.virtual_nodes):
            point = self._hash(f"{node_id}#vn{replica}")
            if self._node_map.get(point) == node_id:
                del self._node_map[point]
                idx = bisect_right(self._ring, point) - 1
                if idx >= 0 and self._ring[idx] == point:
                    self._ring.pop(idx)

    def get_node(self, key: str) -> Optional[str]:
        if not self._ring:
            return None
        point = self._hash(key)
        idx = bisect_right(self._ring, point)
        if idx == len(self._ring):
            idx = 0
        return self._node_map[self._ring[idx]]
