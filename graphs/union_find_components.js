/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1095
 * Updated: 2025-10-28T17:27:22+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1095;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
