# Решение 1 ДЗ по курсу HPC в MADE

## Требования для запуска

1. Python 3.8 или выше.
2. Настроенные зависимости из [requirements.txt](requirements.txt)
3. Установленны [Jupyter Notebook или Lab](https://jupyter.org/)

## Как запустить

```
pip install -r ./requirements.txt
```

DVC стадии, необходимые для работы можно посмотреть через команду:
```
dvc dag
```

Для запуска всех стадий:
```
dvc repro -P
```

## Решение задач

### Предсказание мощности топ 1 суперкомпьютер на 2025

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/KernelA/made-hpc-hw1/blob/master/perf_pred.ipynb)

Открыть [perf_pred.ipynb](perf_pred.ipynb)

### Оценка потребляемого электричества суперкомпьютерами относительно производимого электричества в мире

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/KernelA/made-hpc-hw1/blob/master/energy_estimation.ipynb)

Открыть [energy_estimation.ipynb](energy_estimation.ipynb)


### Улучшение программы для перемножения матриц

Улучшение было сделано с помощью распараллеливания через OpenMP.

Сравнение результатов можно посмотреть [в логах GitHub Actions (стадия Run perfomance test)](https://github.com/KernelA/made-hpc-hw1/actions/workflows/cpp-build.yaml)

Код содержится в [matmul](matmul).

Результаты расчётов на виртуальных машинах в GitHub Actions (runtime kij with OpenMP это ускоренный вариант с добавлением OpenMP):
```
runtime 12.035211 seconds
runtime 12.018422 seconds
runtime 12.140203 seconds
runtime 11.852801 seconds
runtime 12.224198 seconds
average runtime ijk 12.054167 seconds
---------------------------------
runtime 11.819296 seconds
runtime 11.791385 seconds
runtime 11.876471 seconds
runtime 11.791874 seconds
runtime 11.860732 seconds
average runtime jik 11.827952 seconds
---------------------------------
runtime 5.274646 seconds
runtime 5.302574 seconds
runtime 5.324396 seconds
runtime 5.331030 seconds
runtime 5.317554 seconds
average runtime kij 5.310040 seconds
---------------------------------
runtime 4.809488 seconds
runtime 4.735850 seconds
runtime 4.736422 seconds
runtime 4.803046 seconds
runtime 4.796994 seconds
average runtime kij opt 4.776360 seconds
---------------------------------
runtime 2.794244 seconds
runtime 2.655177 seconds
runtime 2.657312 seconds
runtime 2.785687 seconds
runtime 2.755523 seconds
average runtime kij with OpenMP 2.729589 seconds
---------------------------------
```
