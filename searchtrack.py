import pandas as pd
import mysql.connector

def model_price(brand_name):

    conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject") 
    mycursor = conn.cursor()
    mycursor.execute("select *from products")
    row = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    df = pd.DataFrame(row, columns=column_names)
    df = df.drop(['product_id', 'email', 'phonenum', 'img', 'ad_title', 'descp'], axis='columns')


    # Filter the DataFrame to include only rows where the brand matches the passed brand_name
    brand_df = df[df['brand'] == brand_name]
    
    # If there are no rows for the given brand, return a message or handle it accordingly
    if brand_df.empty:
        return f"No models found for the brand '{brand_name}'."
    
    # Get the model with the highest frequency
    most_frequent_model = brand_df['model'].mode().iloc[0]
    
    # Calculate the mean price for the most frequent model
    mean_price = brand_df[brand_df['model'] == most_frequent_model]['price'].mean()
    
    return most_frequent_model, int(mean_price)