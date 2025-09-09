CXX = g++-15
CXXFLAGS = -std=c++17 -O2

all: bench_direct bench_vector bench_indirect

bench_direct: benchmark.cpp sum_direct.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

bench_vector: benchmark.cpp sum_vector.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

bench_indirect: benchmark.cpp sum_indirect.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	rm -f bench_direct bench_vector bench_indirect
