/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 57
 * Updated: 2025-01-11T14:04:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 57;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
