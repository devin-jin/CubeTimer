import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_best_times(ls):
    ls = sorted(ls)
    return ls[0]

def get_ao5(ls):
    if len(ls) < 5: return float('nan')
    else: return sum(ls[-5:])/5

def get_ao12(ls):
    if len(ls) < 12: return float('nan')
    else: return mean(ls[-12:])

