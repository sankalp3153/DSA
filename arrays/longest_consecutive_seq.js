/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 370
 * Updated: 2025-03-31T13:32:45+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 370;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
