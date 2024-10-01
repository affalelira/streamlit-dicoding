import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 

def create_customers_df(df):
    customers_df = df.groupby('customer_city').agg(
        customer_count=('customer_id', 'count')
    ).reset_index()
   
    return customers_df

def visualization_customers_state(customers_df):    
    customers_df = customers_df.sort_values(by='customer_count', ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))  
    colors = ['#004b87']  
    colors += ['#1f77b4', '#4e99c5'] * 4  
    colors = colors[:10] 

    sns.barplot(
        x="customer_count", 
        y="customer_city",
        data=customers_df.head(10),  
        palette=colors,
        ax=ax
    )

    ax.set_title("Top 10 Cities by Number of Customers", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel("Number of Customers", fontsize=12)
    ax.tick_params(axis='y', labelsize=12)
    
    plt.tight_layout()

    return fig

#file main_data dimasukkan ke dalam spreadsheet dikarenakan file mb yang besar sehingga tidak dapat di upload di github 
url = "https://docs.google.com/spreadsheets/d/1PxqLf2Mc__Z5jFKajBhr5fQgNOlSmCx4g1zoRdYFQ3E/gviz/tq?tqx=out:csv"

main_data = pd.read_csv(url)
customers_df = create_customers_df(main_data)

st.set_page_config(page_title="Customer Demographics", page_icon="🌍")

st.markdown("# Customer demographics by city in Brazil")
st.sidebar.header("Customer Demographics")

demography = visualization_customers_state(customers_df)
st.pyplot(demography)

st.write(
    """In this marketplace, most customers come from the city of Sao Paulo, followed by the city of Rio de Janeiro and so on. 
    This is probably because Sao Paulo is the largest economic city in Brazil. """
)



