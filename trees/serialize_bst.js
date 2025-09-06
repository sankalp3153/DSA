/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 931
 * Updated: 2025-09-06T23:39:52+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 931;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
