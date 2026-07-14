/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1966
 * Updated: 2026-07-14T17:33:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1966;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
