/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 954
 * Updated: 2025-09-13T19:48:05+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 954;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
