import streamlit as st 
from urllib.parse import quote
import requests

api_key = st.secrets['API_KEY']

def get_symbols_data(search_queries):
    s1 = search_queries.split(',')
    s2 = [quote(i.strip()) for i in s1]
    url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey={}"
    d = []
    for i in s2:
        data = requests.get(url.format(i, api_key)).json()
        d.append(data)
    return d 

def main():
    st.set_page_config(page_title='Alpha Vantage API', layout='wide')
    st.title("Alpha Vantage Search Symbols API")
    search = st.text_input("Please enter Company names seperated by comma : ")
    button = st.button('Submit')
    if button:

        d = get_symbols_data(search)
        for i in d:
            st.write(i)
            st.write('\n\n')

if __name__ == '__main__':
    main()

    