/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 770
 * Updated: 2025-07-28T22:54:43+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 770;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
