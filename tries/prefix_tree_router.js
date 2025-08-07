/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 802
 * Updated: 2025-08-07T13:13:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 802;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
