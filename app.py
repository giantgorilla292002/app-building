# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:54:05 2024

@author: piyus
"""

import streamlit as st

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers below:")

    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
