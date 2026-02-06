/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1440
 * Updated: 2026-02-06T11:59:04+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1440;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
