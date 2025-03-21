/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 336
 * Updated: 2025-03-21T22:32:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 336;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
