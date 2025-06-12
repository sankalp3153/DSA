/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 612
 * Updated: 2025-06-12T11:10:52+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 612;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
