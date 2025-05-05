import streamlit as st
import random
import time     
import requests #call api 
   
#ui part of streamlit 

st.title("🌈Welcome To Money Making Machine!")

def generate_money():
    return random.randint(1,100) #rantint generate the specific interger between the number with the help of random module

st.subheader("Instant Cash Generator")

if st.button("Generate Money!"):

    st.write("Counting Money....")

    time.sleep(10)    # time module with sleep method delay time 20 second
    
    amount = generate_money()  # store the function in variable  
    
    st.success(f"Your made ${amount}")

#api section
def fetch_data_hustle():
    try:
        response = requests.get("https://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing")
    except:
        return ("Something went wrong")
    
#ui of api
st.subheader("Side Hustles Ideas")

if st.button("Generate Hustle!"):
    idea = fetch_data_hustle()
    st.success(idea)


def fetch_money_quote():
    try:
        response = requests.get("https://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes ["money_quote"]
        else:
            return ("Money is the root of all evils!")
    except:
        return ("Something went wrong!")

st.subheader("Money Making Motivation")
if st.button("Get Inspired!"):
    quote = fetch_money_quote()
    st.success(quote)


