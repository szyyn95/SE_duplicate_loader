# Experiment Overlook

1. Does the type of intermediate task matter? (EXP Code: TYPE<XX>)


2. Does the ratio of target task in the intermediate task matter? (EXP Code: RAT<XX>)

3. Semantic similarity analysis of false negatives / false positives.
**Analysis done from results obtained in TYPE and RAT experiments above.


# Experiment Plan
| EXP_Code | do_pretrain | pretrain_tasks            | CLAIM    |
|----------|-------------|---------------------------|----------|
| TYPE01   | 1           | cola                      |  Yihong  |
| TYPE02   | 1           | sst                       |  Yihong  |
| TYPE03   | 1           | mrpc                      |  Yihong  |
| TYPE04   | 1           | qqp                       |   Ziwei  |
| TYPE05   | 1           | sts                       |   Ziwei  |
| TYPE06   | 1           | mnli                      |   Ziwei  |
| TYPE07   | 1           | qnli                      |   Ziwei  |
| TYPE08   | 1           | rte                       |   Ziwei  |
| TYPE09   | 1           | wnli                      |   Ziwei  |
| TYPE10   | 1           | stov (NOT target dataset) |   Ziwei  |
| -------- | ----------- | ------------------------- | -------- |
| RAT01    | 1           | 0.0 qqp + 1.0 stov        |   Shan   |
| RAT02    | 1           | 0.1 qqp + 0.9 stov        |   Shan   |
| RAT03    | 1           | 0.2 qqp + 0.8 stov        |   Shan   |
| RAT04    | 1           | 0.3 qqp + 0.7 stov        |   Shan   |
| RAT05    | 1           | 0.4 qqp + 0.6 stov        |   Shan   |
| RAT06    | 1           | 0.5 qqp + 0.5 stov        |          |
| RAT07    | 1           | 0.6 qqp + 0.4 stov        |          |
| RAT08    | 1           | 0.7 qqp + 0.3 stov        |          |
| RAT09    | 1           | 0.8 qqp + 0.2 stov        |          |
| RAT10    | 1           | 0.9 qqp + 0.1 stov        |          |
| RAT11    | 1           | 1.0 qqp + 0.0 stov        |          |
<br>
** Please put your name under CLAIM to take the experiment for yourself. You shall idealy claim at least 5 experiments so that the project is divided evenly.<br>
** Name the exp_name in your config file as the EXP_Code in the above table.<br>
** For each of your experiment, please do hyperparameter (i.e. learning rate) tuning. <br>
