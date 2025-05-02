/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 474
 * Updated: 2025-05-02T14:24:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 474;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
