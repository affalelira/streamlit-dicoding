import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 


def create_payment_type(df):
    average_payment_by_type = df.groupby('payment_type').agg(
    average_payment=('payment_value', 'mean'),
    order_count=('order_id', 'count')
    ).reset_index()

    return average_payment_by_type 

def visualization_payment_type(average_payment_by_type):  
    average_payment_by_type = average_payment_by_type.sort_values(by='order_count', ascending=False)

    fig, ax = plt.subplots(figsize=(5, 5))
    plt.pie(
        average_payment_by_type['order_count'],  
        labels=average_payment_by_type['payment_type'],  
        autopct='%1.1f%%',  
        startangle=90,  
        colors=sns.color_palette("Set2", len(average_payment_by_type)),  
        wedgeprops={'edgecolor': 'white'}  
    )

    plt.title("Percentage of Customers by Payment Type", fontsize=16)

    plt.tight_layout()
    
    return(fig)
    
#file main_data dimasukkan ke dalam spreadsheet dikarenakan file mb yang besar sehingga tidak dapat di upload di github 
url = "https://docs.google.com/spreadsheets/d/1PxqLf2Mc__Z5jFKajBhr5fQgNOlSmCx4g1zoRdYFQ3E/gviz/tq?tqx=out:csv"

main_data = pd.read_csv(url)
average_payment_by_type = create_payment_type(main_data)

st.set_page_config(page_title="Payment Type", page_icon="💵")

st.markdown("# Payment Type")
st.sidebar.header("Payment Type")

payment_type = visualization_payment_type(average_payment_by_type)
st.pyplot(payment_type)

st.write(
    """Based on the pie chart results, 73.8% of customers pay using credit_card, 
    19.4% of customers pay with boleto, 5.3% of customers pay with voucher, 
    and 1.4% of customers pay with debit_card. """
)
