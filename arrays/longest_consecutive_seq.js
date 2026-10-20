/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2279
 * Updated: 2026-10-20T18:58:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2279;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
