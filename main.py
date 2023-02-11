"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
  if n <= 1:
    return n
  else:
    next = n//b
    recurrence = a * (simple_work_calc(next, a, b)) + n

  return recurrence

def test_simple_work(): 
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(30, 2, 4) == 48
  assert simple_work_calc(50, 2, 3) == 110
  assert simple_work_calc(50, 3, 2) == 881


def work_calc(n, a, b, f):
  if n <= 1:
    return n
  else:
    next = n//b
    recurrence = a * (work_calc(next, a, b, f)) + f(n)
  
  return recurrence

def span_calc(n, a, b, f):
  if n <= 1:
    return n
  else:
    next = n//b
    recurrence = a * (span_calc(next, a, b, f)) + f(n)
    
  return recurrence


def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(20, 3, 2, lambda n: n*n) == 1114
  assert work_calc(50, 2, 2, lambda n: n) == 276
  assert work_calc(40, 3, 2, lambda n: n*n) == 4942

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
  a = 2
  b = 2
  for n in sizes:
    result.append((
			n,
			work_fn1(n, a, b, lambda n: 1),
			work_fn2(n, a, b, lambda n: n),
      work_fn2(n, a, b, lambda n: int(math.log(a, 10)))))
  return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2', 'W_3'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
  res = compare_work(work_calc, work_calc)
  print(res)

def test_compare_span():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(20, 3, 2, lambda n: n*n) == 1114
  assert work_calc(50, 2, 2, lambda n: n) == 276
  assert work_calc(40, 3, 2, lambda n: n*n) == 4942

print_results(compare_work(span_calc, span_calc))
test_compare_work()