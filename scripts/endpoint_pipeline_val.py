import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://ecdae81c-c4b1-4dd5-98f0-11dd6cadce72.eastus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'RKahbZjn87G14qBpomAFfHpnk02LhPMH'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 30,
            "campaign": 2,
            "cons.conf.idx": -42,
            "cons.price.idx": 93.2,
            "contact": "cellular",
            "day_of_week": "thu",
            "default": "no",
            "duration": 2453,
            "education": "high.school",
            "emp.var.rate": -0.1,
            "euribor3m": 4.076,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "nov",
            "nr.employed": 5195.8,
            "pdays": 999,
            "poutcome": "nonexistent",
            "previous": 0
          },
          {
            "age": 30,
            "campaign": 1,
            "cons.conf.idx": -40.8,
            "cons.price.idx": 92.963,
            "contact": "cellular",
            "day_of_week": "fri",
            "default": "no",
            "duration": 199,
            "education": "university.degree",
            "emp.var.rate": -2.9,
            "euribor3m": 1.268,
            "housing": "no",
            "job": "admin.",
            "loan": "yes",
            "marital": "single",
            "month": "jun",
            "nr.employed": 5076.2,
            "pdays": 3,
            "poutcome": "success",
            "previous": 1
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


