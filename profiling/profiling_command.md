### To generate performance data:
`python -m cProfile -o performance.prof two_loops.py`

### To generate flamegraph:
`flameprof performance.prof > output.svg`