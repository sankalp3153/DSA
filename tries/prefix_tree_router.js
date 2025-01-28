/**
 * Module: prefix_tree_router
 * Approach: character map node transitions
 * Revision: 112
 * Updated: 2025-01-28T18:23:25+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 112;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
