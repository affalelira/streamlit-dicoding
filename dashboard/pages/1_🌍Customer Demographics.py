import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 

def create_customers_df():
    customers_df = pd.read_csv('C:/Users/Affa Lelira Ibrahim/OneDrive/Documents/College UPN/VS Code/submission/data/olist_customers_dataset.csv')
    
    return customers_df

customers_df = create_customers_df()

def visualization_customers_state():
    customers_df = create_customers_df()
    
    customers_state = customers_df.groupby(by="customer_city").customer_id.nunique().reset_index()
    customers_state.rename(columns={"customer_id": "customer_count"}, inplace=True)

    fig, ax = plt.subplots(figsize=(10, 5))  
    colors_ = ["#72BCD4"] + ["#D3D3D3"] * (len(customers_state) - 1) 

    sns.barplot(
        x="customer_count", 
        y="customer_city",
        data=customers_state.sort_values(by="customer_count", ascending=False).head(10),  
        palette=colors_,
        ax=ax
    )

    ax.set_title("Number of Customers by City", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel("Number of Customers", fontsize=12)
    ax.tick_params(axis='y', labelsize=12)
    
    return fig

st.set_page_config(page_title="Customer Demographics", page_icon="🌍")

st.markdown("# Customer demographics by city in Brazil")
st.sidebar.header("Customer Demographics")

demography = visualization_customers_state()
st.pyplot(demography)

st.write(
    """In this marketplace, most customers come from the city of Sao Paulo, followed by the city of Rio de Janeiro and so on. 
    This is probably because Sao Paulo is the largest economic city in Brazil. """
)



