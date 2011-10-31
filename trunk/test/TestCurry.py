from __future__ import with_statement

import os
import sys

import unittest
import logging

import pickle
import shutil
import tempfile

import jsonpickle
import jsonpickle.pickler
import jsonpickle.unpickler

import currypy as CurryModule

def foo(a, b=3):
    return a*b 


class TestPickle(unittest.TestCase):
    """
    """

    def setUp(self):

        self.rootDir = tempfile.mkdtemp()
        self._path = os.path.join(self.rootDir, 'foo')
        return
    
    def tearDown(self):
        if os.path.exists(self.rootDir):
            shutil.rmtree(self.rootDir)
        
        return
    
    
    def testPickle1(self):

        curriedObj = CurryModule.Curry(foo, 2, b=5)
        dumped = False
        with open(self._path, 'w') as f:
            pickle.dump(curriedObj, f)
            dumped =True
        assert dumped

        loaded = False
        with open(self._path, 'r') as f:
            curried = pickle.load(f)
            assert curried() is 10
            loaded = True
        assert loaded

        return

    def testPickle2(self):

        curriedObj = CurryModule.Curry(foo, 2)
        dumped = False
        with open(self._path, 'w') as f:
            pickle.dump(curriedObj, f)
            dumped =True
        assert dumped

        loaded = False
        with open(self._path, 'r') as f:
            curried = pickle.load(f)
            assert curried(b=7) is 14
            loaded = True
        assert loaded

        return


    def testPickle3(self):

        curriedObj = CurryModule.Curry(foo, b=5)
        dumped = False
        with open(self._path, 'w') as f:
            pickle.dump(curriedObj, f)
            dumped =True
        assert dumped

        loaded = False
        with open(self._path, 'r') as f:
            curried = pickle.load(f)
            assert curried(7) is 35
            loaded = True
        assert loaded

        return

        
    # END class TestPickle
    pass


class TestJsonPickle(unittest.TestCase):
    """
    """

    def setUp(self):

        self.rootDir = tempfile.mkdtemp()
        self._path = os.path.join(self.rootDir, 'foo')
        return
    
    def tearDown(self):
        if os.path.exists(self.rootDir):
            shutil.rmtree(self.rootDir)
        
        return

    
    def testJsonPickle1(self):

        pickler = jsonpickle.Pickler()

        curriedObj = CurryModule.Curry(foo, 2, b=5)

        jsonVal = pickler.flatten(curriedObj)

        unpickler = jsonpickle.unpickler.Unpickler()
        newCurriedObj = unpickler.restore(jsonVal)

        self.assertEquals(10, newCurriedObj())

        return

    def testJsonPickle2(self):

        pickler = jsonpickle.Pickler()

        curriedObj = CurryModule.Curry(foo, 2, b=5)

        jsonVal = pickler.flatten(curriedObj)
        dumped = False
        with open(self._path, 'w') as f:
            pickle.dump(jsonVal, f)
            dumped = True
            pass

        loaded = False
        with open(self._path, 'r') as f:
            v = pickle.load(f)
            unpickler = jsonpickle.unpickler.Unpickler()
            newCurriedObj = unpickler.restore(v)
            loaded = True

        self.assertEquals(10, newCurriedObj())

        return

    # END class JsonPickle
    pass

def main():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCase, 'test'))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
    return

if __name__=="__main__":
    main()

