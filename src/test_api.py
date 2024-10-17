import requests

url = "http://localhost:8000/predict"

data = {
    "features": [-1.63980912e+00, -1.26963120e+00, -4.57022763e-02, -1.58577857e-03]
}

# data = {
#     "features": [-1.63980912e+00, -1.26963120e+00]
# }


# try and except block to handle the exception
try:
    response = requests.post(url, json=data)
    print(response.json())
except Exception as e:
    print(e)

