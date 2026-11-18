"""
O(1) Doubly-Linked List + Hash Map LRU Cache.

Time Complexity: O(1) get() and put()
Space Complexity: O(capacity)
"""

from typing import Dict, Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class _Node(Generic[K, V]):
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key: K, val: V) -> None:
        self.key = key
        self.val = val
        self.prev: Optional[_Node[K, V]] = None
        self.next: Optional[_Node[K, V]] = None


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self._map: Dict[K, _Node[K, V]] = {}
        self._head: _Node = _Node(None, None)
        self._tail: _Node = _Node(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node[K, V]) -> None:
        prev_node, next_node = node.prev, node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def _insert_front(self, node: _Node[K, V]) -> None:
        first = self._head.next
        node.prev = self._head
        node.next = first
        self._head.next = node
        if first:
            first.prev = node

    def get(self, key: K) -> Optional[V]:
        node = self._map.get(key)
        if node is None:
            return None
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: K, value: V) -> None:
        if key in self._map:
            node = self._map[key]
            node.val = value
            self._remove(node)
            self._insert_front(node)
            return

        if len(self._map) == self.capacity:
            lru = self._tail.prev
            if lru and lru is not self._head:
                self._remove(lru)
                del self._map[lru.key]

        node = _Node(key, value)
        self._map[key] = node
        self._insert_front(node)
