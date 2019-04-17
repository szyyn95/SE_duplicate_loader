#!/bin/bash

ratios=(0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0)
amount=200000
for r in "${ratios[@]}"; do
    command="python QQP_data_mixer.py --SE_path ./SE_result/intermediate_train.tsv --total_amount ${amount} --ratio ${r}"
    echo ${command}
    eval ${command}
done