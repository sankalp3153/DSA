/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 149
 * Updated: 2025-02-03T20:45:02+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 149;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
