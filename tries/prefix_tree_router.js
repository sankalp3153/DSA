/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 158
 * Updated: 2025-02-06T16:47:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 158;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
