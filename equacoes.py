import streamlit as st
import pandas as pd
import numpy as np
import math
import sympy as sp

x = sp.Symbol('x')
eq = st.text_input('Type your equation here: ')
if eq:
    func = sp.diff(eq, x)
    st.write(eq)