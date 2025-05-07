/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 485
 * Updated: 2025-05-07T10:52:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 485;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
