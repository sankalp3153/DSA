/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 540
 * Updated: 2025-05-23T11:05:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 540;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
