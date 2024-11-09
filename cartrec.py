import pandas as pd
import mysql.connector
from kneed import KneeLocator
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt



def predict_cluster(brand, model, price, kf):
    # Create a DataFrame with the provided inputs
    frm = pd.DataFrame([[brand, model, price]], columns=['brand', 'model', 'price'])
    
    # Generate dummy variables for 'brand' and 'model'
    frm = pd.get_dummies(frm, columns=['brand', 'model'])
    
    # Reindex to ensure it has the same columns as the model's training data
    frm = frm.reindex(columns=kf.feature_names_in_, fill_value=0)
    
    # Predict the cluster
    return kf.predict(frm)[0]

def extract_brand_model(df, b, m):
    # List of possible brand and model columns
    brands = b
    models = m
    
    # Extract the columns for brands and models
    brand_columns = [col for col in df.columns if col in brands]
    model_columns = [col for col in df.columns if col in models]
    
    if not brand_columns or not model_columns:
        raise ValueError("Dummy variable columns for 'brand' or 'model' are missing.")
    
    # Extract the brand and model names based on the dummy variables
    brand = df[brand_columns].idxmax(axis=1).str.strip()
    model = df[model_columns].idxmax(axis=1).str.strip()
    
    # Create a new DataFrame with brand, model, price, and cluster
    result_df = pd.DataFrame({
        'brand': brand,
        'model': model,
        'price': df['price'],
        'cluster': df['Cluster']
    })
    
    return result_df

def showclusters(df, elbow_point, clust):
    for i in range(elbow_point):
        if i == clust:
            df3 = df[df['cluster'] == i]
            break

    return df3

def rec(mail):
    conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
    mycursor = conn.cursor()
    mycursor.execute("select *from products")
    row = mycursor.fetchall()

    column_names = [desc[0] for desc in mycursor.description]
    df = pd.DataFrame(row, columns=column_names)

    df = df.drop(['product_id', 'email', 'phonenum', 'img', 'ad_title', 'descp'], axis='columns')
    # print(df)

    df_brands = list(df['brand'])
    df_models = list(df['model'])

    dv = pd.concat([pd.get_dummies(df['brand']), pd.get_dummies(df['model'])], axis='columns')
    df = pd.concat([dv,df], axis='columns')
    df = df.drop(['brand', 'model'], axis='columns')

    # print(f"\n\n {df}")

    k_range = range(1,10)
    sse = []
    for i in k_range: 
      kf = KMeans(n_clusters=i)
      kf.fit(df)
      sse.append(kf.inertia_)


    # plt.title('Elbow Plot')
    # plt.xlabel('K')
    # plt.ylabel('SSE')
    # plt.plot(k_range,sse)
    # plt.show()

    kneedle = KneeLocator(k_range, sse, curve='convex', direction='decreasing')
    elbow_point = kneedle.elbow

    # print(f"\n\n Elbow Point = {elbow_point}")  

    kf = KMeans(n_clusters=elbow_point)
    df['Cluster'] = kf.fit_predict(df)  

    # print(f"\n\n {df}")

    query = 'select *from useractivity where email=%s'
    mycursor.execute(query,(mail,))
    row2 = mycursor.fetchone()
    # print(f"\n\n {predict_cluster(row2[2], row2[3],row2[4], kf)}")

    if row2[5] == 0:
       return row
    else:
        df1 = extract_brand_model(df, df_brands, df_models)
        df3 = showclusters(df1, elbow_point, predict_cluster(row2[2], row2[3], row2[4], kf))

        brand_list = df3['brand'].tolist()
        model_list = df3['model'].tolist()
        price_list = df3['price'].tolist()

        format_strings = ','.join(['%s'] * len(brand_list))
        query = f"SELECT * FROM products WHERE brand IN ({format_strings}) AND model IN ({format_strings}) AND price IN ({format_strings})"
        mycursor.execute(query, tuple(brand_list + model_list + price_list))

        result_rows = mycursor.fetchall()
        return result_rows

    

 

