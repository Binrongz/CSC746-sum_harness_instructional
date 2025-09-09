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
   printf(" inside sum_vector problem_setup, N=%lld \n", N);

   // Initialize A[i]
   for (int64_t i = 0; i < N; ++i) {
      A[i] = i;
   }
}

float
sum(int64_t N, float A[])
{
   printf(" inside sum_vector perform_sum, N=%lld \n", N);
   
   // Traverse A sequentially, adding A[i] to total each time
   int64_t total = 0;

   for (int64_t i = 0; i < N; ++i) {
      total += A[i];
   }

   return total;
}

