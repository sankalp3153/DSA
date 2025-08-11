/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 825
 * Updated: 2025-08-11T19:21:26+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 825;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
