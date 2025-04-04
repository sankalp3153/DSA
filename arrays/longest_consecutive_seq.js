/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 393
 * Updated: 2025-04-04T20:19:32+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 393;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
