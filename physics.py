import math
import cmath

h = 6.62607015e-34
hbar = h / (2 * math.pi)

def sqrt(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return cmath.sqrt(x)

def tunnel(E, V0, m, a):
    if E > V0:
        return (0, "%")
    else:
        k = (sqrt((2 * m) * (V0 - E))) / hbar
        T = (math.e ** (-2 * k * a)) * 100
        return f"{T}%"

def entangle(s00, s01, s10, s11, A):
    if A == 0:
        prob0 = (s00 / (s00 + s01)) * 100
        prob1 = (s01 / (s00 + s01)) * 100
        return f"Probability of B = 0 | {prob0}%\nProbability of B = 1 | {prob1}%"
    elif A == 1:
        prob0 = (s10 / (s10 + s11)) * 100
        prob1 = (s11 / (s10 + s11)) * 100
        return f"Probability of B = 0 | {prob0}\nProbability of B = 1 | {prob1}"
    else:
        return "Please enter a 1 or 0 for A"

def wave(WavR, WavI, E, time):
    theta = (E * time) / hbar
    return f"Real = {((WavR * math.cos(theta)) + (WavI * math.sin(theta)))}\nImaginary = {((WavI * math.cos(theta)) - (WavR * math.sin(theta)))}"

def Energy(m, L, n):
    return ((n ** 2) * (h ** 2)) / ((8 * m) * (L ** 2))