/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 503
 * Updated: 2025-05-10T14:42:56+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 503;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
