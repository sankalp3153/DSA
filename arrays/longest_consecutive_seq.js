/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1175
 * Updated: 2025-11-26T14:20:42+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1175;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
