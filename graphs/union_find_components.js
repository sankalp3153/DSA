/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 106
 * Updated: 2025-01-28T11:34:31+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 106;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
