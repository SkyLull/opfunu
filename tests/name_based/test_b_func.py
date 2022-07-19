#!/usr/bin/env python
# Created by "Thieu" at 20:42, 18/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import numpy as np
import opfunu
import pytest


def test_BartelsConn_results():
    ndim = 10
    problem = opfunu.name_based.BartelsConn(ndim=ndim)
    x = np.ones(ndim)
    result = problem.evaluate(x)
    assert isinstance(problem, opfunu.name_based.Benchmark)
    assert isinstance(problem.lb, np.ndarray)
    assert len(problem.lb) == ndim
    assert problem.bounds.shape[0] == ndim
    assert len(problem.x_global) == ndim


def test_Beale_results():
    ndim = 2
    problem = opfunu.name_based.Beale(ndim=ndim)
    x = np.ones(ndim)
    result = problem.evaluate(x)
    assert isinstance(problem, opfunu.name_based.Benchmark)
    assert isinstance(problem.lb, np.ndarray)
    assert len(problem.lb) == ndim
    assert problem.bounds.shape[0] == ndim
    assert len(problem.x_global) == ndim


def test_BiggsExp02_results():
    ndim = 2
    problem = opfunu.name_based.BiggsExp02(ndim=ndim)
    x = np.ones(ndim)
    result = problem.evaluate(x)
    assert isinstance(problem, opfunu.name_based.Benchmark)
    assert isinstance(problem.lb, np.ndarray)
    assert len(problem.lb) == ndim
    assert problem.bounds.shape[0] == ndim
    assert len(problem.x_global) == ndim


def test_BiggsExp03_results():
    ndim = 3
    problem = opfunu.name_based.BiggsExp03(ndim=ndim)
    x = np.ones(ndim)
    result = problem.evaluate(x)
    assert isinstance(problem, opfunu.name_based.Benchmark)
    assert isinstance(problem.lb, np.ndarray)
    assert len(problem.lb) == ndim
    assert problem.bounds.shape[0] == ndim
    assert len(problem.x_global) == ndim








