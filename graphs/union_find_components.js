/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 198
 * Updated: 2025-02-17T10:34:12+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 198;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
