/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 2084
 * Updated: 2026-08-19T18:23:58+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2084;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
