# n1zamrus-quadratic-equation-python

Точный решатель уравнения `a*x² + b*x + c = 0` для целых коэффициентов.

## Контракт

- Коэффициенты принимаются как десятичные строки или Python `int`.
- Десятичные строки могут содержать не менее 10 000 цифр. Парсер не вызывает
  `int` на всей строке, поэтому не зависит от лимита `sys.set_int_max_str_digits`.
- Решения классифицируются как `two_real`, `double_real`, `two_complex`,
  `one_real`, `no_solution` или `all_reals`.
- Все решения хранятся точно: рациональные корни используют `Fraction`, а
  иррациональные и комплексные корни — нормализованную форму
  `rational +/- coefficient*sqrt(radicand)` с необязательным `i`.
- `float` не используется для дискриминанта, сравнения с нулём или вывода.

## Использование

```python
from quadratic_equation import solve

result = solve("1", "-3", "2")
print(result.status)  # two_real
print([root.expression() for root in result.roots])  # ['2', '1']
```

CLI принимает `a`, `b` и `c` как аргументы:

```bash
python quadratic_equation.py 1 -3 2
```

## Проверка

```bash
make test
```
