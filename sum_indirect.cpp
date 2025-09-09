#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

void 
setup(int64_t N, float A[])
{
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);

   // Random seed and Mersenne Twister
   std::random_device rd;
   std::mt19937 gen(rd());

   // Uniformly distributed in [0, N-1]
   std::uniform_int_distribution<> distr(0, N - 1);

   // Fill A[i] with a random integer in the range [0, N-1]
   for (int64_t i = 0; i < N; i++) {
      A[i] = distr(gen);
   }
}

float
sum(int64_t N, float A[])
{
   printf(" inside sum_indirect perform_sum, N=%lld \n", N);

   int64_t total = 0;   // Accumulate the result
   int64_t index = 0;  // Start from 0

   for (int64_t i = 0; i < N; i++) {
      index = A[index];    // Jump to the position specified by A[index]
      total += index;      // Add the index value at this position to the sum
   }

   return total;
}

