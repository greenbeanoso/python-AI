# # streamlit_app.py
# import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# url = "https://docs.google.com/spreadsheets/d/14y-4NsxulqiP7oDh6a0oAjoZgnvMWE7SDdsP9sa7b9s/edit?usp=sharing"


# # Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)

# df = conn.read(spreadsheet=url, usecols=[0, 1])

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")
# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/14y-4NsxulqiP7oDh6a0oAjoZgnvMWE7SDdsP9sa7b9s/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)
# st.dataframe(data)
for row in data.itertuples():
    st.write(f"{row.name} has a {row.pet}")
