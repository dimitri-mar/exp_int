import streamlit as st
import os
import numpy as np


if 'username' not in st.session_state:
    print("This is a new user!")
    username = f"user_{np.random.randint(100000000000)}"
    st.session_state['username'] = username
else:
    print("I already know you!")
    username = st.session_state['username']

filename = f"{username}.dat"



if os.path.exists(f"{username}.dat"):
    with open(filename, "r" ) as f:
        user_number = int(f.readlines()[0])
        print(user_number)
    st.write(f"you already submitted the number {user_number}, user {username}")
else:

    user_number = st.slider('Pick a number', 1, 100)
    st.write('The current number is ', user_number)
    st.write('Your username is  ', username)

    if st.button('submit'):
        st.write('Number submitted')
        with open(filename, "w" ) as f:
            print("the user number is ", user_number, "user", username)
            f.write(str(user_number))
        st.experimental_rerun()
