from time import time
from typing import Iterable
import logging


class SimpleTimer:
    """
    Simple class to compare execution time of two functions or to compute it given a function.
    """
    def __init__(self, args: Iterable, func, compare_to=None, log_file_name=None):
        _iter = iter(args)
        if not '__iter__' in dir(_iter.__next__()):
            args = ((x,) for x in args)
        self.args = args
        self.func = func
        self.compare_to = compare_to
        logging.basicConfig(level=logging.INFO, filename=log_file_name, format="%(levelname)s: %(message)s")

    def simple_timing(self):
        logging.info("+" + "*" * 48 + "+")
        logging.info("Times for function %s" % self.func.__name__)
        for arg in self.args:
            logging.info(f"{'Testcase':<10}: {arg}")
            try:
                start = time()
                r = self.func(*arg)
                elapsed = time() - start
                logging.info(f"{'Time':<10}: {elapsed:.9f}s  return: {r}")
            except Exception as e:
                logging.error(f"Error on execution", exc_info=True)
        logging.info("+" + "*" * 48 + "+")

    def compare(self):
        def timer(func, *args, **kwargs):
            try:
                start = time()
                rf = func(*args, **kwargs)
                elapsed = time() - start
                logging.info(f"{func.__name__:<{fmt + 9}}: {elapsed:.9f}s  return: {rf}")
            except Exception as e:
                logging.error(f"Error on execution", exc_info=True)
        fmt = max(len(self.func.__name__), len(self.compare_to.__name__))
        logging.info("+" + "*" * 48 + "+")
        logging.info("Times for functions %s and %s:" % (self.func.__name__, self.compare_to.__name__))
        for arg in self.args:
            timer(self.func, *arg)
            timer(self.compare_to, *arg)
        logging.info("+" + "*" * 48 + "+")

    def __call__(self):
        if self.compare_to is None:
            self.simple_timing()
        else:
            self.compare()
