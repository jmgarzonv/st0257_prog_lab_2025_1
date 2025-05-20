# Test Basic

import os
import unittest
import importlib
from threading import Thread

expected_module = 'RENDEZVOUSMODULE'
default_module = 'pysync'

if expected_module in os.environ:
    rendezvous_mdl = os.environ[expected_module]
else:
    rendezvous_mdl = 'pysync'

rendezvous_imprt = importlib.__import__(rendezvous_mdl, globals(), locals(), [], 0)

class TestProdConsTestSync(unittest.TestCase):

    def __thread(rendezvous,value):
        return rendezvous.echanger(value)
    
    def test_basic_concur(self):
        rendezvous = rendezvous_imprt.RendezvousDEchange()
        val_1 = 1
        val_2 = 2
        thread_1 = Thread(target=__thread, args=(val_1,))
        thread_2 = Thread(target=__thread, args=(val_2,))
        thread_1.start()
        thread_2.start()
        ret_thr_1 = thread_1.join()
        ret_thr_2 = thread_2.join()
        
        self.assertNotEqual(ret_thr_1, val_2)
        self.assertNotEqual(ret_thr_2, val_1)
