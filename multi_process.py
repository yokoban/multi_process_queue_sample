from concurrent import futures
import multiprocessing
from datetime import  datetime
import logging
import time
import queue
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format=('%(processName)s %(message)s'))
formatter = '%(processName)s, %(message)s'

w1 = logging.getLogger('woker1')
w1.setLevel(logging.DEBUG)
fh1 = logging.FileHandler('./process1.log', 'w')
fh1.setFormatter(logging.Formatter(formatter))
fh1.setLevel(logging.DEBUG)
w1.addHandler(fh1)


w2 = logging.getLogger('woker2')
w2.setLevel(logging.DEBUG)
fh2 = logging.FileHandler('./process2.log', 'w')
fh2.setFormatter(logging.Formatter(formatter))
fh2.setLevel(logging.DEBUG)
w2.addHandler(fh2)



w3 = logging.getLogger('woker2')
w3.setLevel(logging.DEBUG)
fh3 = logging.FileHandler('./process3.log', 'w')
fh3.setFormatter(logging.Formatter(formatter))
fh3.setLevel(logging.DEBUG)
w3.addHandler(fh3)


def shared_worker1(num, que, logger):
    print(f'shared worker1 start')
    for i in range(num):
        que.put(f'{multiprocessing.current_process().name}: {i:2d}')
        logger.debug(f'add {i}')
    # data.put(None)



def shared_worker2(data, logger):
    d = []
    while True:
        if not data.empty():
            res = data.get()
            # time.sleep(1)
        else:
            logger.debug('worker3 queue empty')
            break

        d.append(res)
        logger.debug(f'worker3: {res}')

    logger.debug(f'worker3 process end')
    return d





if __name__ == '__main__':
    q = multiprocessing.Manager().Queue(-1)

    logging.debug(f'process start {datetime.now()}')
    with futures.ProcessPoolExecutor(max_workers=3) as executor:
        logging.debug(f'pr1 start')
        pr1 = executor.submit(shared_worker1, 10, q, w1)
        logging.debug(f'pr2 start')
        pr2 = executor.submit(shared_worker1, 10, q, w2)
        logging.debug(f'pr3 start')
        pr3 = executor.submit(shared_worker2, q, w3)


    logging.debug(f'\n\nprocess end   {datetime.now()}')
