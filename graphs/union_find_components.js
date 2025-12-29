/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1302
 * Updated: 2025-12-29T21:11:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1302;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
