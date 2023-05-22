from fastapi import FastAPI
from predrequest import PredictionRequest
import pickle
import numpy as np
import pandas as pd
import uvicorn
import sklearn
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
pickle_in = open("random_forest_model.pickle","rb")
random_forest_model=pickle.load(pickle_in)
print(sklearn.__version__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return{'example':'ex'}

@app.post('/predict')
async def predict(data:PredictionRequest):
    data = data.dict()
    print(data)
    Clear=data['Clear']
    Distance=data['Distance']
    City_Freq=data['City_Freq']
    State_Freq=data['State_Freq']
    Day_of_Year=data['Day_of_Year']
    Temperature=data['Temperature']
    Wind_Speed=data['Wind_Speed']

    prediction = random_forest_model.predict([[Clear,Distance,City_Freq,State_Freq,Day_of_Year,Temperature,Wind_Speed]])
    print(prediction.dtype)

    return{'prediction':prediction.tolist()}



