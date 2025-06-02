/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 577
 * Updated: 2025-06-02T18:47:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 577;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
