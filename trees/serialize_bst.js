/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1920
 * Updated: 2026-07-01T22:52:02+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1920;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
