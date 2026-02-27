/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 1515
 * Updated: 2026-02-27T17:03:36+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1515;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
