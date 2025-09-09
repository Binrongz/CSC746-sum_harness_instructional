#!/bin/bash

mkdir -p logs

executables=("bench_direct" "bench_vector" "bench_indirect")

for exe in "${executables[@]}"; do
    echo "Running $exe..."
    for i in {1..5}; do
        echo "Run $i for $exe"
        echo "========== Run $i for $exe ==========" >> logs/${exe}.log
        ./$exe >> logs/${exe}.log
        echo "" >> logs/${exe}.log
    done
done

