#!/usr/bin/env python
# Created by "Thieu" at 15:44, 04/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import opfunu
import numpy as np

## Test CEC2013 F1
print("====================F1")
problem = opfunu.cec_based.F12013(ndim=50)
x = np.ones(50)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))
