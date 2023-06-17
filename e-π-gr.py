#!/usr/bin/env python
# coding: utf-8

# In[2]:


# For π

import time
from mpmath import mp
import pyautogui

def calculate_pi():
    mp.dps = 9999  # Precision
    pi_str = str(mp.pi)[2:]  # Remove the 3. prefix from pi string
    return pi_str

def fun_0():
    pyautogui.moveTo(100, 100)

def fun_1():
    pyautogui.moveTo(200, 200)

def fun_2():
    pyautogui.moveTo(300, 300)

def fun_3():
    pyautogui.moveTo(400, 400)

def fun_4():
    pyautogui.moveTo(500, 500)

def fun_5():
    pyautogui.moveTo(600, 600)

def fun_6():
    pyautogui.moveTo(700, 700)

def fun_7():
    pyautogui.moveTo(800, 800)

def fun_8():
    pyautogui.moveTo(900, 900)

def fun_9():
    pyautogui.moveTo(1000, 1000)

def display_realtime_pi(pi_digits):
    idx = 0
    try:
        while True:
            digit = pi_digits[idx]
            print(f"\r... {digit} ...", end="")
            if digit == "0":
                fun_0()
            elif digit == "1":
                fun_1()
            elif digit == "2":
                fun_2()
            elif digit == "3":
                fun_3()
            elif digit == "4":
                fun_4()
            elif digit == "5":
                fun_5()
            elif digit == "6":
                fun_6()
            elif digit == "7":
                fun_7()
            elif digit == "8":
                fun_8()
            elif digit == "9":
                fun_9()
            idx = (idx + 1) % len(pi_digits)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

pi_digits = calculate_pi()
display_realtime_pi(pi_digits)


# In[4]:


# For e

import time
from mpmath import mp
import pyautogui

def calculate_e():
    mp.dps = 9999  # Precision
    e_str = str(mp.e)[2:]  # Remove the 2. prefix from e string
    return e_str

def fun_0():
    pyautogui.moveTo(100, 100)

def fun_1():
    pyautogui.moveTo(200, 200)

def fun_2():
    pyautogui.moveTo(300, 300)

def fun_3():
    pyautogui.moveTo(400, 400)

def fun_4():
    pyautogui.moveTo(500, 500)

def fun_5():
    pyautogui.moveTo(600, 600)

def fun_6():
    pyautogui.moveTo(700, 700)

def fun_7():
    pyautogui.moveTo(800, 800)

def fun_8():
    pyautogui.moveTo(900, 900)

def fun_9():
    pyautogui.moveTo(1000, 1000)

def display_realtime_e(e_digits):
    idx = 0
    try:
        while True:
            digit = e_digits[idx]
            print(f"\r... {digit} ...", end="")
            if digit == "0":
                fun_0()
            elif digit == "1":
                fun_1()
            elif digit == "2":
                fun_2()
            elif digit == "3":
                fun_3()
            elif digit == "4":
                fun_4()
            elif digit == "5":
                fun_5()
            elif digit == "6":
                fun_6()
            elif digit == "7":
                fun_7()
            elif digit == "8":
                fun_8()
            elif digit == "9":
                fun_9()
            idx = (idx + 1) % len(e_digits)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

e_digits = calculate_e()
display_realtime_e(e_digits)


# In[6]:


# For phi (φ)

import time
from mpmath import mp
import pyautogui

def calculate_phi():
    mp.dps = 9999  # Precision
    phi_str = str(mp.phi)[2:]  # Remove the 1. prefix from the golden ratio string
    return phi_str

def fun_0():
    pyautogui.moveTo(100, 100)

def fun_1():
    pyautogui.moveTo(200, 200)

def fun_2():
    pyautogui.moveTo(300, 300)

def fun_3():
    pyautogui.moveTo(400, 400)

def fun_4():
    pyautogui.moveTo(500, 500)

def fun_5():
    pyautogui.moveTo(600, 600)

def fun_6():
    pyautogui.moveTo(700, 700)

def fun_7():
    pyautogui.moveTo(800, 800)

def fun_8():
    pyautogui.moveTo(900, 900)

def fun_9():
    pyautogui.moveTo(1000, 1000)

def display_realtime_phi(phi_digits):
    idx = 0
    try:
        while True:
            digit = phi_digits[idx]
            print(f"\r... {digit} ...", end="")
            if digit == "0":
                fun_0()
            elif digit == "1":
                fun_1()
            elif digit == "2":
                fun_2()
            elif digit == "3":
                fun_3()
            elif digit == "4":
                fun_4()
            elif digit == "5":
                fun_5()
            elif digit == "6":
                fun_6()
            elif digit == "7":
                fun_7()
            elif digit == "8":
                fun_8()
            elif digit == "9":
                fun_9()
            idx = (idx + 1) % len(phi_digits)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

phi_digits = calculate_phi()
display_realtime_phi(phi_digits)

