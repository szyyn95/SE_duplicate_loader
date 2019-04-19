# Experiment Overlook

1. Does the type of intermediate task matter? (EXP Code: TYPE<XX>)


2. Does the ratio of target task in the intermediate task matter? (EXP Code: RAT<XX>)

3. Semantic similarity analysis of false negatives / false positives.
**Analysis done from results obtained in TYPE and RAT experiments above.


# Experiment Plan
| EXP_Code | do_pretrain | pretrain_tasks            | CLAIM    | acc_f1 | acc | f1  | precision | recall  |
|----------|-------------|---------------------------|----------|--------|-----|-----|-----------|---------|
| NAIVE    | 0           | none (also no train on target)|   XZ |0.491   |0.405|0.576| 0.405     |1.000    |
| BASE     | 0           | none                      |   XZ     |0.904   |0.916|0.893| 0.921     |0.867    |
| TYPE01   | 1           | cola   (SingleClf)        |   XZ     |0.897   |0.911|0.884| 0.929     |0.843    |
| TYPE02   | 1           | sst   (SingelClf)         |    Ziwei |0.901   |0.913|0.890| 0.912     |0.868    |
| TYPE03   | 1           | mrpc      (PairClf)       |  Ziwei   |0.892   |0.904|0.879| 0.896     |0.864    |
| TYPE04   | 1           | qqp            (PairClf)  |   Ziwei  |0.900   |0.912|0.088| 0.918     |0.868    |
| TYPE05   | 1           | sts-b      (PairReg)      |   XZ     |0.907   |0.918|0.895| 0.923     |0.870    |
| TYPE06   | 1           | mnli     (PairClf)        |   XZ     |0.897   |0.911|0.884| 0.929     |0.843    |
| TYPE07   | 1           | qnli     (PairClf)        |   Ziwei  |        |     |     |           |         | 
| TYPE08   | 1           | rte     (PairClf)         |   Ziwei  |0.899   |0.911|0.888| 0.908     |0.868    |
| TYPE09   | 1           | wnli      (PairClf)       |   Ziwei  |0.298   |0.595|0.000| 0.000     |0.000    |
| TYPE10   | 1           | stov (NOT target dataset) |   Ziwei  |Duplicate w/ RAT01|     |     |           |         |
| RAT01    | 1           | 0.0 qqp + 1.0 stov        |   Yihong |        |     |     |           |         |
| RAT02    | 1           | 0.1 qqp + 0.9 stov        |   Yihong |        |     |     |           |         |
| RAT03    | 1           | 0.2 qqp + 0.8 stov        |   Yihong |        |     |     |           |         |
| RAT04    | 1           | 0.3 qqp + 0.7 stov        |   Yihong |        |     |     |           |         |
| RAT05    | 1           | 0.4 qqp + 0.6 stov        |   Yihong |        |     |     |           |         |
| RAT06    | 1           | 0.5 qqp + 0.5 stov        |   Yihong |        |     |     |           |         |
| RAT07    | 1           | 0.6 qqp + 0.4 stov        |   Shan   |0.880   |0.895|0.865|0.901      |0.832    |
| RAT08    | 1           | 0.7 qqp + 0.3 stov        |   Shan   |0.897   |0.909|0.884|0.911      |0.859    |
| RAT09    | 1           | 0.8 qqp + 0.2 stov        |   Shan   |0.896   |0.909|0.884|0.908      |0.862    |
| RAT10    | 1           | 0.9 qqp + 0.1 stov        |   Shan   |0.896   |0.910|0.883|0.925      |0.845    |
| RAT11    | 1           | 1.0 qqp + 0.0 stov        |   Shan   |0.881   |0.896|0.865|0.907      |0.827    |
<br>
** Please put your name under CLAIM to take the experiment for yourself. You shall idealy claim at least 5 experiments so that the project is divided evenly.<br>
** Name the exp_name in your config file as the EXP_Code in the above table.<br>
** For each of your experiment, please do hyperparameter (i.e. learning rate) tuning. <br>
