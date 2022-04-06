# import numpy as np
from flask import Flask, request, jsonify
# import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)


# Load the model
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return "hello world"


def predict1(list2):
    data = {"product name": ["bat", "ball", "iphone", "charger", "snacks"],
            "product price": [12, 15, 99945, np.NaN, 80],
            "tags": ["sports", "sports", "sports", "electronic", "food"], "rating": [4500, 4000, 600, 70, 5000]}
    df = pd.DataFrame(data)
    print(df)
    # print("list2: " + list2)
    df.set_index('product name', inplace=True)

    list1 = []
    # list2=["sports","electronic","food"]
    for i in range(0, len(list2)):
        print(len(list2))
    for tgs in list2:
        df23 = df[df['tags'] == tgs]
        print(tgs)
        df24 = df23.sort_values(by=['rating'], ascending=False)
        df25 = df24[:2]
        df26 = df25.head()
        list1 += list(df26.index.values)
    print(list1)
    return list1


@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    list1 = request.form.get('taglist')
    m = ""
    list3 = []
    for i in range(1, len(list1)):
        if list1[i] == "'":
            continue
        elif list1[i] == "," or list1[i] == "]":
            m1 = str(m)
            print(type(m1))
            list3.append(m1)
            m = ""
        else:
            m = m + list1[i]

            # print(m)

    # list1=["sports","electronic","food"]
    # Make prediction using model loaded from disk as per the data.
    # input_query = np.array(list1)
    result1 = predict1(list3)
    print(list3)
    # print(list3)
    print(result1)

    # result = model.predict(input_query)
    # Take the first value of prediction
    #  result1 = result
    return jsonify({'values': result1})


if __name__ == '__main__':
    app.run(debug=True)
