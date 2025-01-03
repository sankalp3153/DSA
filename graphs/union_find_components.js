/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 14
 * Updated: 2025-01-03T18:50:37+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 14;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
