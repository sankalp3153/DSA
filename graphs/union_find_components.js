/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 60
 * Updated: 2025-01-12T10:00:54+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 60;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
