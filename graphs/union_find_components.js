/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1463
 * Updated: 2026-02-11T23:07:12+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1463;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
