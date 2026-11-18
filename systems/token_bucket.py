"""
Thread-safe Token Bucket Rate Limiter.

Models burst-tolerant API & carrier gateway rate limiting (e.g., max 100 req/s
with burst capacity of 200).

Time Complexity: O(1) per allow() call
Space Complexity: O(K) for K distinct tenant/API keys
"""

import threading
import time
from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class _Bucket:
    tokens: float
    last_refill: float


class TokenBucketLimiter:
    def __init__(
        self,
        rate_per_second: float,
        capacity: float,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        if rate_per_second <= 0 or capacity <= 0:
            raise ValueError("rate_per_second and capacity must be positive")
        self.rate = rate_per_second
        self.capacity = capacity
        self._clock = clock
        self._buckets: Dict[str, _Bucket] = {}
        self._lock = threading.Lock()

    def allow(self, key: str, cost: float = 1.0) -> bool:
        if cost <= 0:
            return True
        now = self._clock()
        with self._lock:
            bucket = self._buckets.get(key)
            if bucket is None:
                bucket = _Bucket(tokens=self.capacity, last_refill=now)
                self._buckets[key] = bucket

            elapsed = max(0.0, now - bucket.last_refill)
            bucket.tokens = min(self.capacity, bucket.tokens + elapsed * self.rate)
            bucket.last_refill = now

            if bucket.tokens >= cost:
                bucket.tokens -= cost
                return True
            return False
