We provide an auto-generator that can convert the paper list (csv) to markdown. 
When adding new papers, please add them in "data/papers.csv", then run generator.py to update "README.md".
Benchmark time-performance charts can be maintained in "data/benchmark_results.csv". This is a beta feature. The generator reads this file, creates one all-baselines SVG chart per benchmark under "assets/benchmarks/", and embeds matching charts below each problem section. The CSV keeps only core benchmark fields and main-experiment points within benchmark-specific gap bounds (3.5% for TSP-500, 5% otherwise); slower same-method points are kept only when they improve gap.

p.s.
1. When adding a paper containing more than one problem, please use ";" to separate them in the first column.
2. When adding a problem that has accepted abbreviations, please add it to the "abbr" map at the beginning of generator.py.
3. Benchmark runtime should be stored in "time_1000_instances_sec"; optional raw context can be kept in "original_time_text", "time_basis_original", and "n_instances_original".
