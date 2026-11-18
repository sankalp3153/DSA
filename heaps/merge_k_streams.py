"""
K-Way Sorted Stream Merger using a min-heap tournament.
Time: O(N log k) | Space: O(k)
"""

import heapq
from typing import Iterable, Iterator, List, Tuple, TypeVar

T = TypeVar("T")


def merge_k_streams(streams: List[Iterable[T]]) -> Iterator[T]:
    iterators = [iter(stream) for stream in streams]
    heap: List[Tuple[T, int]] = []

    for idx, it in enumerate(iterators):
        first = next(it, None)
        if first is not None:
            heapq.heappush(heap, (first, idx))

    while heap:
        val, idx = heapq.heappop(heap)
        yield val
        nxt = next(iterators[idx], None)
        if nxt is not None:
            heapq.heappush(heap, (nxt, idx))
