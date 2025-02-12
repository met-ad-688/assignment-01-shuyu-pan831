#!/bin/bash
grep -i "python" data/*.csv | wc -l > _output/count_python.txt

