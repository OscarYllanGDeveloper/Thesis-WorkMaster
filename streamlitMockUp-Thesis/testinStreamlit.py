import streamlit as st

import pandas as pd
table = pd.DataFrame( {"Column 1": [1,2,3,4,5], "Column 2": [6,7,8,9,10]})
st.title("This is a Streamlit App")
st.subheader(" This is a Subheader")
st.header(" Now this is a header")
st.text("This should be a Normal Text")
st.table(table)
st.markdown("[New Learning Era](https://wwww.newlearningera.com)")
st.markdown("---")
st.latex("\begin{matrix}a&b&c\\d&e&f\\end{matrix}")
json={"q":"1,2,3,4","w": "5,6,7,8"}
st.json(json)

code= """
print("Holaaa)
def funcion1(lm):
    return 5**lm
"""
st.code(code)

#st.write("")