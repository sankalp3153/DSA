import test from "node:test";
import assert from "node:assert/strict";

import { longestConsecutive } from "../arrays/longest_consecutive_seq.js";
import { maxArea } from "../two_pointers/container_most_water.js";
import { searchRotated } from "../binary_search/rotated_sorted_array.js";
import { BSTNode, serializeBST, deserializeBST } from "../trees/serialize_bst.js";
import { DisjointSet } from "../graphs/union_find_components.js";
import { editDistance } from "../dp/edit_distance.js";
import { PrefixTrie } from "../tries/prefix_tree_router.js";

test("core JS algorithms pass", () => {
  assert.equal(longestConsecutive([100, 4, 200, 1, 3, 2]), 4);
  assert.equal(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
  assert.equal(searchRotated([4, 5, 6, 7, 0, 1, 2], 0), 4);

  const root = new BSTNode(5, new BSTNode(3, new BSTNode(2)), new BSTNode(7));
  const raw = serializeBST(root);
  assert.equal(serializeBST(deserializeBST(raw)), raw);

  const dsu = new DisjointSet(4);
  dsu.union(0, 1);
  dsu.union(2, 3);
  assert.equal(dsu.components, 2);

  assert.equal(editDistance("horse", "ros"), 3);

  const trie = new PrefixTrie();
  trie.insert("/api/v1/messages", "messages_handler");
  assert.equal(trie.search("/api/v1/messages"), "messages_handler");
  assert.equal(trie.startsWith("/api/v1"), true);
});
