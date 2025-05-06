/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 480
 * Updated: 2025-05-06T16:54:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 480;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
