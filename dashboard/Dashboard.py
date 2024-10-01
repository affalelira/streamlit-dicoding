import streamlit as st


st.set_page_config(
    page_title="Olist E-Commerce",
    page_icon="🛒",
)

st.image("C:/Users/Affa Lelira Ibrahim/Downloads/1_1k72mg1_CZvLptX77zzKTg.png")

st.markdown("# Brazilian E-Commerce Public Dataset by Olist")

st.sidebar.success("Select a pages above.")

st.markdown(
    """
    **Olist** is a unicorn company founded by **Tiago Dalvi** in ​​Brazil that operates in the retail sector and has been established since 2015. 
    Olist is usually known as Olist Store, which connects retailers to online marketplaces to help sellers sell their products easily so they can streamline inventory management.
    
    In this streamlit, there are insights about, 
    - Demographics of olist customers in Brazil
    - Best and Worst Performing Product Categories by Number of Orders
    - Best Performing Product Categories by Total Payment
    - Percentage of Customers by Payment Type
    - Recency, Frequency, Monetary Analyzis 

    To see those insights, just **👈select pages from the side bar** 
"""
)

st.sidebar.caption('Affa Lelira Ibrahim | m296b4kx0149@bangkit.academy')