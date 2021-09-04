import math
import numpy as np
from scipy.special import lambertw as W

def get_linear():
    microseconds_in_a_second = 1e6
    return {
        "second": 1 * microseconds_in_a_second,
        "minute": 60 * microseconds_in_a_second,
        "hour": 60 * 60 * microseconds_in_a_second,
        "month": 24 * 30 * 60 * 60 * microseconds_in_a_second,
        "year": 24 * 365 * 60 * 60 * microseconds_in_a_second,
        "century": 100 * 24 * 365 * 60 * 60 * microseconds_in_a_second
    }

def get_log():
    # note - can't actually run this, will inf out
    microseconds_in_a_second = 1e6    
    return {
        "second": 1 * math.exp(microseconds_in_a_second),
        "minute": 60 * math.exp(microseconds_in_a_second),
        "hour": 60 * 60 * math.exp(microseconds_in_a_second),
        "month": 24 * 30 * 60 * 60 * math.exp(microseconds_in_a_second),
        "year": 24 * 365 * 60 * 60 * math.exp(microseconds_in_a_second),
        "century": 100 * 24 * 365 * 60 * 60 * math.exp(microseconds_in_a_second)
    }

def get_sqrt():
    microseconds_in_a_second = 1e6    
    return {
        "second": 1 * math.pow(microseconds_in_a_second, 2),
        "minute": 60 * math.pow(microseconds_in_a_second, 2),
        "hour": 60 * 60 * math.pow(microseconds_in_a_second, 2),
        "month": 24 * 30 * 60 * 60 * math.pow(microseconds_in_a_second, 2),
        "year": 24 * 365 * 60 * 60 * math.pow(microseconds_in_a_second, 2),
        "century": 100 * 24 * 365 * 60 * 60 * math.pow(microseconds_in_a_second, 2)
    }

def get_n_log_n():
    # inverse from wolfram alpha:
    # https://www.wolframalpha.com/input/?i=inverse+of+n+log+n
    microseconds_in_a_second = 1e6    
    return {
        "second": 1 * (microseconds_in_a_second)/W(microseconds_in_a_second)
        "minute": 60 * (microseconds_in_a_second)/W(microseconds_in_a_second),
        "hour": 60 * 60 * (microseconds_in_a_second)/W(microseconds_in_a_second),
        "month": 24 * 30 * 60 * 60 * (microseconds_in_a_second)/W(microseconds_in_a_second),
        "year": 24 * 365 * 60 * 60 * (microseconds_in_a_second)/W(microseconds_in_a_second),
        "century": 100 * 24 * 365 * 60 * 60 * (microseconds_in_a_second)/W(microseconds_in_a_second)
    }

def get_n_squared():
    microseconds_in_a_second = 1e6    
    return {
        "second": 1 * math.pow(microseconds_in_a_second, 0.5),
        "minute": 60 * math.pow(microseconds_in_a_second, 0.5),
        "hour": 60 * 60 * math.pow(microseconds_in_a_second, 0.5),
        "month": 24 * 30 * 60 * 60 * math.pow(microseconds_in_a_second, 0.5),
        "year": 24 * 365 * 60 * 60 * math.pow(microseconds_in_a_second, 0.5),
        "century": 100 * 24 * 365 * 60 * 60 * math.pow(microseconds_in_a_second, 0.5)
    }

def get_n_cubed():
        microseconds_in_a_second = 1e6    
    return {
        "second": 1 * math.pow(microseconds_in_a_second, 1/3),
        "minute": 60 * math.pow(microseconds_in_a_second, 1/3),
        "hour": 60 * 60 * math.pow(microseconds_in_a_second, 1/3),
        "month": 24 * 30 * 60 * 60 * math.pow(microseconds_in_a_second, 1/3),
        "year": 24 * 365 * 60 * 60 * math.pow(microseconds_in_a_second, 1/3),
        "century": 100 * 24 * 365 * 60 * 60 * math.pow(microseconds_in_a_second, 1/3)
    }

def get_two_to_the_n():
    microseconds_in_a_second = 1e6    
    return {
        "second": 1 * math.log2(microseconds_in_a_second),
        "minute": 60 * math.log2(microseconds_in_a_second),
        "hour": 60 * 60 * math.log2(microseconds_in_a_second),
        "month": 24 * 30 * 60 * 60 * math.log2(microseconds_in_a_second),
        "year": 24 * 365 * 60 * 60 * math.log2(microseconds_in_a_second),
        "century": 100 * 24 * 365 * 60 * 60 * math.log2(microseconds_in_a_second)
    }

def max_steps(size):
    product = 1
    count = 0
    for i in range(2, size):
        product *= i
        if product > size:
            return count
        count += 1
        
def get_n_factorial():
    # there is no inverse for the factorial :(
    # I could approximate it, but python might not be up for the challenge.
    microseconds_in_a_second = 1e6    
    return {
        "second": max_steps(1 * microseconds_in_a_second),
        "minute": max_steps(60 * microseconds_in_a_second),
        "hour": max_steps(60 * 60 * microseconds_in_a_second),
        "month": max_steps(24 * 30 * 60 * 60 * microseconds_in_a_second),
        "year": max_steps(24 * 365 * 60 * 60 * microseconds_in_a_second),
        "century": max_steps(100 * 24 * 365 * 60 * 60 * microseconds_in_a_second)
    }


