/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 181
 * Updated: 2025-02-12T15:15:15+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 181;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
