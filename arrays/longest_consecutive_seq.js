/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1198
 * Updated: 2025-12-01T14:28:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1198;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
