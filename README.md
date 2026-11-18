# Distributed Systems Primitives & Core Algorithms

Production-oriented implementations of core algorithms, data structures, and backend systems primitives written in **Python** and **JavaScript (ES6+)**, complete with complexity analysis and automated tests.

## Structure

| Module | Highlights | Language |
| :--- | :--- | :--- |
| `systems/` | Consistent Hashing Ring (virtual nodes), Token Bucket Rate Limiter, O(1) LRU Cache | Python |
| `arrays/` | Prefix-sum Subarray Sum K, Product Except Self, In-place Matrix Rotation, Longest Consecutive Sequence | Python / JS |
| `sliding_window/` | Minimum Window Substring, Monotonic Deque Sliding Window Maximum | Python |
| `graphs/` | Dijkstra Shortest Path (min-heap), Kahn Topological Sort, Disjoint Set Union-Find | Python / JS |
| `dp/` | Patience Sorting LIS `O(n log n)`, Bottom-Up Coin Change, Rolling-Row Edit Distance | Python / JS |
| `heaps/` | K-Way Stream Merger, Dual-Heap Running Median | Python |
| `trees/` | Binary Tree Maximum Path Sum, Preorder BST Codec | Python / JS |
| `tries/` | Prefix Tree Router with wildcard/prefix matching | JavaScript |
| `two_pointers/` | Three Sum, Container With Most Water | Python / JS |
| `binary_search/` | Median of Two Sorted Arrays `O(log(min(m,n)))`, Rotated Array Search | Python / JS |
| `intervals/` & `greedy/` | Interval Coalescing, Circular Gas Tour | Python |

## Running Tests

```bash
python3 -m unittest discover -s tests -v
node --test tests/algorithms.test.mjs
```
