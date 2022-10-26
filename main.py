
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return "hello world"


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
        elif list1[i] == " " and  list1[i - 1] == ",":
            continue
        else:
            m = m + list1[i]

    result1 = predict1(list3)
    print(list3)
    # print(list3)
    print(result1)

    return jsonify({'values': result1})


def predict1(list2):
    import pandas as pd
    import json
    import numpy as np

    json1 = '''{
      "-N-ErPNmOHE4KwkctEDH": {
        "category": "mobile",
        "product_price": "139900",
        "rating": "950"
      },
      "-N-Ery8rwKA-Sq9UA5OM": {
        "category": "mobile",
        "product_price": "109999",
        "rating": "945"
      },
      "-N-H_ulYGfyvqztiVw7J": {
        "category": "mobile",
        "product_price": "66999",
        "rating": "940"
      },
      "-N-Hae2ygs4-heBjC68v": {
        "category": "mobile",
        "product_price": "71900",
        "rating": "944"
      },
      "-N-HatGGnPri06yULqMp": {
        "category": "laptop",
        "product_price": "77990",
        "rating": "940"
      },
      "-N-HbgTPnhx5jJUD8rj0": {
        "category": "laptop",
        "product_price": "129989",
        "rating": "941"
      },
      "-N-HcP3q9adxbza9LFjp": {
        "category": "laptop",
        "product_price": "239900",
        "rating": "450"
      },
      "-N-HcrcbTvyIT9_DAhe8": {
        "category": "laptop",
        "product_price": "60499",
        "rating": "440"
      },
      "-N-HdMReNyhJsRF7xDqY": {
        "category": "sports",
        "product_price": "3999",
        "rating": "450"
      },
      "-N-HeHhbqJIqZtEpgKsq": {
        "category": "sports",
        "product_price": "1499",
        "rating": "445"
      },
      "-N-HepqmXveuSveMgsP4": {
        "category": "sports",
        "product_price": "1499",
        "rating": "946"
      },
      "-N-HgAJ4g0ex7ZijWPap": {
        "category": "sports",
        "product_price": "999",
        "rating": "449"
      },
      "-N-Hhh2rNUW_8Hur4GTw": {
        "category": "sports",
        "product_price": "11988",
        "rating": "451"
      },
      "-N-HicEX4GVOlN-7K2Mr": {
        "category": "electronic",
        "product_price": "11999",
        "rating": "449"
      },
      "-N-Hj9EcJqPF_OejlbUR": {
        "category": "electronic",
        "product_price": "20999",
        "rating": "451"
      },
      "-N-Hjyet8fjqM8tFW95K": {
        "category": "electronic",
        "product_price": "2999",
        "rating": "445"
      },
      "-N-Hkj0cjQR4l3Tvv9Hr": {
        "category": "electronic",
        "product_price": "4999",
        "rating": "444"
      },
      "-N-HmRPameJwcvbJqlWy": {
        "category": "others",
        "product_price": "6499",
        "rating": "440"
      },
      "-N-Ho16GWJp2xLPiKN0Q": {
        "category": "others",
        "product_price": "2499",
        "rating": "444"
      },
      "-N-HoeYud9rdEhuz1y3D": {
        "category": "others",
        "product_price": "3799",
        "rating": "449"
      },
      "-N-Hpic4k6l1-cEOUiqW": {
        "category": "others",
        "product_price": "5299",
        "rating": "452"
      },
      "-N-HqHtpZU2net8VsaRb": {
        "category": "others",
        "product_price": "45990",
        "rating": "451"
      }
    }'''

    df = pd.read_json(json1, orient='index')
    print(df)

    # input11 = ["sports", "electronic"]
    # list2 = input11
    list1 = []
    for tgs in list2:
        df23 = df[df['category'] == tgs]
        # print(df23)
        df24 = df23.sort_values(by=['rating'], ascending=False)
        df25 = df24[:2]
        df26 = df25.head()

        list1.append(df26.index.values)

    m = np.array(list1, dtype=list)
    output11 = m.flatten().tolist()
    print(output11)

    for i in range(0, len(list2)):
        print(len(list2))

    return output11


if __name__ == '__main__':
    app.run(debug=True)
