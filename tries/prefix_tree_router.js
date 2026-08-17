/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 2067
 * Updated: 2026-08-17T15:28:50+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2067;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
