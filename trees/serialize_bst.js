/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1667
 * Updated: 2026-04-12T11:12:39+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1667;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
