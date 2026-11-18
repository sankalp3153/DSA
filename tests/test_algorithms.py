import unittest

from arrays.product_except_self import product_except_self
from arrays.rotate_matrix import rotate_matrix
from arrays.subarray_sum_equals_k import subarray_sum
from binary_search.median_two_sorted import find_median_sorted_arrays
from dp.coin_change_min import coin_change
from dp.longest_increasing_subseq import length_of_lis
from graphs.network_delay_dijkstra import network_delay_time
from graphs.topological_schedule import topological_order
from greedy.circular_tour_gas import can_complete_circuit
from heaps.median_data_stream import MedianStream
from heaps.merge_k_streams import merge_k_streams
from intervals.merge_overlapping import merge_intervals
from sliding_window.min_window_substring import min_window
from sliding_window.sliding_window_max import max_sliding_window
from systems.consistent_hash import ConsistentHashRing
from systems.lru_cache import LRUCache
from systems.token_bucket import TokenBucketLimiter
from trees.max_path_sum import TreeNode, max_path_sum
from two_pointers.three_sum_zero import three_sum


class TestCoreAlgorithmsAndSystems(unittest.TestCase):
    def test_consistent_hash_ring(self):
        ring = ConsistentHashRing(virtual_nodes=64)
        for node in ("broker-1", "broker-2", "broker-3"):
            ring.add_node(node)
        assigned = {ring.get_node(f"tenant-{i}") for i in range(100)}
        self.assertEqual(assigned, {"broker-1", "broker-2", "broker-3"})
        ring.remove_node("broker-2")
        self.assertNotIn("broker-2", {ring.get_node(f"tenant-{i}") for i in range(100)})

    def test_token_bucket_limiter(self):
        now = [0.0]
        limiter = TokenBucketLimiter(rate_per_second=2.0, capacity=2.0, clock=lambda: now[0])
        self.assertTrue(limiter.allow("tenant-1"))
        self.assertTrue(limiter.allow("tenant-1"))
        self.assertFalse(limiter.allow("tenant-1"))
        now[0] += 0.5
        self.assertTrue(limiter.allow("tenant-1"))

    def test_lru_cache(self):
        cache: LRUCache[str, int] = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)
        cache.put("c", 3)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("c"), 3)

    def test_arrays_and_windows(self):
        self.assertEqual(subarray_sum([1, 1, 1], 2), 2)
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(rotate_matrix([[1, 2], [3, 4]]), [[3, 1], [4, 2]])
        self.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_graphs_dp_heaps_trees(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0)
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(topological_order(4, [(1, 0), (2, 0), (3, 1), (3, 2)]), [0, 1, 2, 3])
        self.assertEqual(network_delay_time([(2, 1, 1), (2, 3, 1), (3, 4, 1)], 4, 2), 2)
        self.assertEqual(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(list(merge_k_streams([[1, 4, 7], [2, 5], [3, 6]])), [1, 2, 3, 4, 5, 6, 7])
        ms = MedianStream()
        for v in (1, 2, 3):
            ms.add(v)
        self.assertEqual(ms.median(), 2.0)
        root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(max_path_sum(root), 42)
        self.assertEqual(merge_intervals([(1, 3), (2, 6), (8, 10)]), [(1, 6), (8, 10)])
        self.assertEqual(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)


if __name__ == "__main__":
    unittest.main()
