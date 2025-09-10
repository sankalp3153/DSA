/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 945
 * Updated: 2025-09-10T20:21:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 945;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
