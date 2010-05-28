import jug.compound
import jug.mapreduce
import numpy as np
from jug.backends.dict_store import dict_store
from jug.compound import *
from tests.test_mapreduce import mapper, reducer, dfs_run
def test_compound():
    jug.task.Task.store = dict_store()
    A = np.random.rand(10000)
    x = CompoundTask(jug.mapreduce.mapreduce,reducer, mapper, A)
    dfs_run(x)
    y = CompoundTask(jug.mapreduce.mapreduce,reducer, mapper, A)

    assert y.can_load()
    assert y.result == x.result

