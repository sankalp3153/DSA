/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 2159
 * Updated: 2026-09-05T20:50:17+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2159;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
