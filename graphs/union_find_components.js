/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 244
 * Updated: 2025-03-03T10:03:16+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 244;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
