import time
from A_increase import RangeIterable
from B_decrease import RangeIterableIterator
from C_sinus import SinusIterableWithGenerator
import itertools
# создаем цепочку итераторов из предыдущих заданий
main_iter = itertools.chain(
    RangeIterableIterator(32),
    RangeIterable(16),
    SinusIterableWithGenerator(64, 32)
)
for line in main_iter:
    print(line)
    time.sleep(0.25)
