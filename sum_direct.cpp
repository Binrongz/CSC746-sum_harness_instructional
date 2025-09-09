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
   printf(" inside direct_sum problem_setup, N=%lld \n", N);
}

float
sum(int64_t N, float A[])
{
   printf(" inside direct_sum perform_sum, N=%lld \n", N);

   // Computes sum of i=0...N-1 using only the loop index variable
   int64_t total = 0;
   for(int i = 0; i < N; i++) {
      total += i;
   }
   return total;
}

