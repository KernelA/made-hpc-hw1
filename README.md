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

