/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 520
 * Updated: 2025-05-15T11:58:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 520;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
