/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 290
 * Updated: 2025-03-12T19:18:53+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 290;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
