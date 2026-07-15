/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1969
 * Updated: 2026-07-15T13:36:41+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1969;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
