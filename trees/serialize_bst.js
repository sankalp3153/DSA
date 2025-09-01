/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 908
 * Updated: 2025-09-01T11:01:28+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 908;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
