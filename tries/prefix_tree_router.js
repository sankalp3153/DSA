/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 549
 * Updated: 2025-05-24T13:39:11+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 549;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
