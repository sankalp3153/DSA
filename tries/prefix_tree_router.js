/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 1607
 * Updated: 2026-03-24T19:44:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1607;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
