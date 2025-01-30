/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 129
 * Updated: 2025-01-30T15:17:19+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 129;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
