/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 333
 * Updated: 2025-03-21T17:34:31+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 333;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
