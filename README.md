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

## Использование Python API

```python
from quadratic_equation import solve

result = solve("1", "-3", "2")
print(result.status)  # two_real
print([root.expression() for root in result.roots])  # ['2', '1']
```

CLI принимает `a`, `b` и `c` как аргументы. Человеко-читаемый режим явно
показывает статус и список точных корней:

```bash
python3 quadratic_equation.py 1 -3 2
# status: two_real
# roots:
# - 2
# - 1
```

Для интеграций доступен JSON-режим. Все корни остаются строками, поэтому JSON
не теряет точность на больших числах:

```bash
python3 quadratic_equation.py 1 2 5 --json
# {"status": "two_complex", "roots": ["-1 + 2i", "-1 - 2i"]}
```

Допустимые статусы: `two_real`, `double_real`, `two_complex`, `one_real`,
`no_solution` и `all_reals`. Некорректный коэффициент печатается в stderr,
а процесс завершается с кодом `2`. Пустые строки, `NaN`, десятичные дроби,
подчёркивания и другие нецелые значения отклоняются.

Пример с коэффициентом в 10 000 цифр не требует специального флага:

```bash
python3 quadratic_equation.py 1 0 "-$(python3 -c 'print("1" + "0" * 9999)')"
```

Команда использует только строковые аргументы и точные целые операции.

## Проверка

```bash
make test
```
