/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1161
 * Updated: 2025-11-24T12:25:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1161;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
