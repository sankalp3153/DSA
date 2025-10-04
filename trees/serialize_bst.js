/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1023
 * Updated: 2025-10-04T20:47:11+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1023;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
