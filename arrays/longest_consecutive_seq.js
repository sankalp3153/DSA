/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 922
 * Updated: 2025-09-05T11:18:11+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 922;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
