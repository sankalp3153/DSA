/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1782
 * Updated: 2026-05-20T13:59:33+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1782;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
