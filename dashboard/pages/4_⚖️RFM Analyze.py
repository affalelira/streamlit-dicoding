import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 

def create_rfm_df(df):
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    rfm_df = df.groupby(by="customer_unique_id", as_index=False).agg({
        "order_purchase_timestamp": "max",  
        "order_id": "nunique",             
        "payment_value": "sum"              
    })
    
    rfm_df.columns = ["customer_unique_id", "max_order_timestamp", "frequency", "monetary"]
    rfm_df["max_order_timestamp"] = pd.to_datetime(rfm_df["max_order_timestamp"])
    recent_date = df["order_purchase_timestamp"].dt.date.max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].dt.date.apply(lambda x: (recent_date - x).days)

    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)

    return rfm_df

def visualization_rfm_df(rfm_df):  
    rfm_df['short_customer_id'] = rfm_df['customer_unique_id'].apply(lambda x: f"{x[:5]}...{x[-5:]}")

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 6))

    colors = ["#72BCD4"] * 5

    sns.barplot(y="frequency", x="short_customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("By Frequency", loc="center", fontsize=18)
    ax[0].tick_params(axis='x', labelsize=15)
    ax[0].tick_params(axis='x', rotation=45)  

    sns.barplot(y="monetary", x="short_customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title("By Monetary", loc="center", fontsize=18)
    ax[1].tick_params(axis='x', labelsize=15)
    ax[1].tick_params(axis='x', rotation=45)  

    plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=20)
    plt.tight_layout()
    
    return fig

def visualization_recency(rfm_df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(rfm_df['recency'], bins=30, kde=True)  
    plt.title("Histogram of Recency", fontsize=16)
    plt.xlabel("Recency (days)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
   
    return(fig)

#file main_data dimasukkan ke dalam spreadsheet dikarenakan file mb yang besar sehingga tidak dapat di upload di github 
url = "https://docs.google.com/spreadsheets/d/1PxqLf2Mc__Z5jFKajBhr5fQgNOlSmCx4g1zoRdYFQ3E/gviz/tq?tqx=out:csv"

main_data = pd.read_csv(url)

rfm_df = create_rfm_df(main_data)

st.set_page_config(page_title="RFM Analyze", page_icon="⚖️")

st.markdown("# Frequency & Monetary Analyze")
st.sidebar.header("RFM Analyze")

rfm = visualization_rfm_df(rfm_df)
st.pyplot(rfm)

st.write(
    """
    Two distinct types of customers can be identified: 

    1. **High-frequency customers who contribute low monetary value** 
    2. **Infrequent customers whose transactions are of high value**

    Understanding these customer profiles enables the development of tailored marketing strategies. 
    For instance, special offers can be designed to reward high-frequency customers, 
    while premium services can be offered to those who bring in significant revenue from their fewer transactions.
     """
)

st.markdown("# Recency Analyze")

recency = visualization_recency(rfm_df)
st.pyplot(recency)

st.write(
    """
    Two distinct types of customers can be identified: 

    1. **Customers within the 0-100 day range are recognized as loyal and active.** 
    To enhance their purchasing frequency, businesses can implement strategies such as exclusive discounts, loyalty programs, and targeted. 

    2. **Customers falling in the 200-300 day range tend to make infrequent repeat purchases.**
    In this case, effective strategies include offering special discounts and sending reminders about products
    they may have previously considered or purchased. 

"""
)


