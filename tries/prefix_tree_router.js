/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 296
 * Updated: 2025-03-13T20:09:14+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 296;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
