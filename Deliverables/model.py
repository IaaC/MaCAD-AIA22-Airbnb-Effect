
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import joblib
import pickle
import json 


def call():

    with open('input.json') as f:
        data = json.load(f)

    lat = data['lat']
    lon = data['lon']
    listing = data['listing']
    sqm = data['sqm']


    data = pd.read_csv(r"D:\MACAD TERM 3\Studio\airbnb\ann_final.csv")

    X = data.loc[:,'latitude':'PerSqm']

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    X_scaled_df = pd.DataFrame(X_scaled)

    y = data.iloc[:,4].to_numpy()

    y = y.reshape(-1, 1)

    from sklearn.preprocessing import MinMaxScaler
    scalerY = MinMaxScaler()

    Y_scaled = scalerY.fit_transform(y)

    Y_scaled_df = pd.DataFrame(Y_scaled)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test, data_train, data_test = train_test_split(X_scaled, Y_scaled, data, test_size = 0.2, random_state = 42)

    import sklearn

    from sklearn.kernel_ridge import KernelRidge
    model = KernelRidge(kernel = "polynomial", degree = 6)

    model.fit(X_train, y_train)

    import pickle
    filename = 'test.sav'
    pickle.dump(model, open(filename, 'wb'))
    

    scalerX_filename = "scalerXAtoB.save"
    joblib.dump(scaler, scalerX_filename)

    scalerY_filename = "scalerYAtoB.save"
    joblib.dump(scalerY, scalerY_filename)

    data_test.info()

    path = 'test.sav'

    model = pickle.load(open(path, 'rb'))

    scalerX = joblib.load("scalerXAtoB.save")
    scalerY = joblib.load("scalerYAtoB.save")




    
    new_data = pd.DataFrame([[lat,lon,listing,sqm]])
    scaled_input = scalerX.transform(new_data)
    out = model.predict(scaled_input)
    predictions = scalerY.inverse_transform(out)
    pred_list = predictions.tolist()
    flat_list = []

    for i in pred_list:
        flat_list += i
    R = flat_list[0]

    dev = {
    "deviation": R
    }

    print(dev)

    with open("output.json", 'w') as f:
        json.dump(dev, f)
    f.close()

call()

    



