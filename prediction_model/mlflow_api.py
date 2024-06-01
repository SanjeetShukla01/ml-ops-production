import mlflow.pyfunc

model_name = "Prediction_model_LR"
stage = 'Staging'
model=mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")

model.predict([[1.,1.,0.,1.,0.,4.55387689,360.,1.,2.,8.25556865]])