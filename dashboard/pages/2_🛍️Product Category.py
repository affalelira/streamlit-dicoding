import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 


def create_product_category(df):
    grouped_category_df = df.groupby('product_category_name').agg(
        order_count=('order_id', 'count')
    ).reset_index()

    return grouped_category_df

def create_product_category_total_payment(df):
    total_payment_by_category = df.groupby('product_category_name').agg(
    total_payment=('payment_value', 'sum'),
    order_count=('order_id', 'count')
    ).reset_index()

    return total_payment_by_category 

def visualization_product_category(grouped_category_df):  
    grouped_category_df = grouped_category_df.sort_values(by='order_count', ascending=False)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    colors = ["#72BCD4"] + ["#D3D3D3"] * 4 

    sns.barplot(
        x="order_count", 
        y="product_category_name", 
        data=grouped_category_df.head(5),  
        palette=colors, 
        ax=ax[0]
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Order Count", fontsize=12)
    ax[0].set_title("Best Performing Product Categories", loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.barplot(
        x="order_count", 
        y="product_category_name", 
        data=grouped_category_df.tail(5), 
        palette=colors, 
        ax=ax[1]
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Order Count", fontsize=12)
    ax[1].invert_xaxis()  
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Worst Performing Product Categories", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)

    plt.suptitle("Best and Worst Performing Product Categories by Number of Orders", fontsize=20)
    plt.tight_layout()

    return fig

def visualization_product_category_total_payment(total_payment_by_category):
    total_payment_by_category = total_payment_by_category.sort_values(by='total_payment', ascending=False)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    colors = ["#72BCD4"] + ["#D3D3D3"] * 4  

    sns.barplot(
        x="total_payment", 
        y="product_category_name", 
        data=total_payment_by_category.head(5),  
        palette=colors, 
        ax=ax[0]
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Total Payment", fontsize=12)
    ax[0].set_title("Best Performing Product Categories by Total Payment", loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.barplot(
        x="total_payment", 
        y="product_category_name", 
        data=total_payment_by_category.tail(5),  
        palette=colors, 
        ax=ax[1]
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Total Payment", fontsize=12)
    ax[1].invert_xaxis()  
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Worst Performing Product Categories by Total Payment", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)

    plt.suptitle("Best and Worst Performing Product Categories by Total Payment", fontsize=20)

    plt.tight_layout()

    return(fig)

main_data = pd.read_csv("C:/Users/Affa Lelira Ibrahim/OneDrive/Documents/College UPN/VS Code/submission/dashboard/main_data.csv")
grouped_category_df = create_product_category(main_data)
total_payment_by_category =  create_product_category_total_payment(main_data)

st.set_page_config(page_title="Product Category", page_icon="🛍️")

st.markdown("# Product Category")
st.sidebar.header("Product Category")

product_category = visualization_product_category(grouped_category_df)
st.pyplot(product_category)

st.write(
    """In general, there was a significant demand for household items like bed and beauty products. 
    Conversely, physical media, including CDs and DVDs, as well as 
    niche categories such as PC gaming products, experienced a downturn in popularity. 
    This shift could be attributed to technological advancements and evolving consumer preferences."""
)

st.markdown("# Product Category by Total Payment")

product_category_total_payment = visualization_product_category_total_payment(total_payment_by_category)
st.pyplot(product_category_total_payment)

st.write(
    """Household product categories lead the market in both the number of orders and total payment, showcasing their immense popularity. 
    In contrast, pc gaming products, while limited in order volume, attract a high transaction value, highlighting their status as premium items. 
    Conversely, the performance of the CDs and DVDs, security and services category has faltered, reflecting a significant shift 
    in consumer preferences towards digital alternatives and other services beyond this platform. """
)


