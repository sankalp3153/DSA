/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 1147
 * Updated: 2025-11-19T17:23:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1147;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
