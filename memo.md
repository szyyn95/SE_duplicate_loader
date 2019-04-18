# Experiment Overlook

1. Does the type of intermediate task matter? (EXP Code: TYPE<XX>)


2. Does the ratio of target task in the intermediate task matter? (EXP Code: RAT<XX>)

3. Semantic similarity analysis of false negatives / false positives.
**Analysis done from results obtained in TYPE and RAT experiments above.


# Experiment Plan
| EXP_Code | do_pretrain | pretrain_tasks            | CLAIM    |
|----------|-------------|---------------------------|----------|
| NAIVE    | 0           | none (also no train on target)                  |   XZ     |
| BASE     | 0           | none                      |   XZ     |
| TYPE01   | 1           | cola   (SingleClf)        |   XZ     |
| TYPE02   | 1           | sst   (SingelClf)         |    Ziwei |
| TYPE03   | 1           | mrpc      (PairClf)       |  Ziwei   |
| TYPE04   | 1           | qqp            (PairClf)  |   Ziwei  |
| TYPE05   | 1           | sts-b      (PairReg)      |   XZ     |
| TYPE06   | 1           | mnli     (PairClf)        |   XZ     |
| TYPE07   | 1           | qnli     (PairClf)        |   Ziwei  |
| TYPE08   | 1           | rte     (PairClf)         |   Ziwei  |
| TYPE09   | 1           | wnli      (PairClf)       |   Ziwei  |
| TYPE10   | 1           | stov (NOT target dataset) |   Ziwei  |
| -------- | ----------- | ------------------------- | -------- |
| RAT01    | 1           | 0.0 qqp + 1.0 stov        |   Yihong |
| RAT02    | 1           | 0.1 qqp + 0.9 stov        |   Yihong |
| RAT03    | 1           | 0.2 qqp + 0.8 stov        |   Yihong |
| RAT04    | 1           | 0.3 qqp + 0.7 stov        |   Yihong |
| RAT05    | 1           | 0.4 qqp + 0.6 stov        |   Yihong |
| RAT06    | 1           | 0.5 qqp + 0.5 stov        |   Yihong |
| RAT07    | 1           | 0.6 qqp + 0.4 stov        |   Shan   |
| RAT08    | 1           | 0.7 qqp + 0.3 stov        |   Shan   |
| RAT09    | 1           | 0.8 qqp + 0.2 stov        |   Shan   |
| RAT10    | 1           | 0.9 qqp + 0.1 stov        |   Shan   |
| RAT11    | 1           | 1.0 qqp + 0.0 stov        |   Shan   |
<br>
** Please put your name under CLAIM to take the experiment for yourself. You shall idealy claim at least 5 experiments so that the project is divided evenly.<br>
** Name the exp_name in your config file as the EXP_Code in the above table.<br>
** For each of your experiment, please do hyperparameter (i.e. learning rate) tuning. <br>
