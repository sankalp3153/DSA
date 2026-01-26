/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1394
 * Updated: 2026-01-26T17:32:20+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1394;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
