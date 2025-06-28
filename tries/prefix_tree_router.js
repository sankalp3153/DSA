/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 687
 * Updated: 2025-06-28T20:53:30+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 687;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
