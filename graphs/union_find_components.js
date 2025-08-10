/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 819
 * Updated: 2025-08-10T23:24:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 819;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
