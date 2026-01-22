/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 1377
 * Updated: 2026-01-22T21:00:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1377;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
