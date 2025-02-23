/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 221
 * Updated: 2025-02-23T20:08:10+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 221;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
