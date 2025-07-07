/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 701
 * Updated: 2025-07-07T18:57:20+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 701;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
