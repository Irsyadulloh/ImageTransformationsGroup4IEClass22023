import streamlit as st

st.title("👥 Group Members")

st.write("### Meet the Team")

col1, col2, col3, col4 = st.columns(4)

# Add group member details
with col1:
    st.image("C:/Users/Lenovo/Downloads/Streamlit Transformation App/images/Muhammad Yusuf Irsyadulloh.png", caption="Member 1", width=200)
    st.write("**Name**: Muhammas Yusuf Irsyadulloh\n**SID**: 004202300040")

with col2:
    st.image("C:/Users/Lenovo/Downloads/Streamlit Transformation App/images/Syarifa Nuraini.jpg", caption="Member 2", width=200)
    st.write("**Name**: Syarifa Nuraini\n**SID**: 004202300028")

with col3:
    st.image("C:/Users/Lenovo/Downloads/Streamlit Transformation App/images/Maria Dianata.png", caption="Member 3", width=200)
    st.write("**Name**: Maria Dianata\n**SID**: 004202300084")

with col4:
    st.image("C:/Users/Lenovo/Downloads/Streamlit Transformation App/images/Bunga Gembira.jpg", caption="Member 4", width=200)
    st.write("**Name**: Bunga Gembira\n**SID**: 004202300037")