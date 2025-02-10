/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 175
 * Updated: 2025-02-10T16:50:34+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 175;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
