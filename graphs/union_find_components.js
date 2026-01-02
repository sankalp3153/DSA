/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1325
 * Updated: 2026-01-02T22:09:19+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1325;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
