/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 563
 * Updated: 2025-05-28T12:02:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 563;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
