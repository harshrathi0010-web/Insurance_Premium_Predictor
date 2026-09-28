


import pickle
import pandas  as pd 
import numpy as np

# Import the ML model.
with open('model/model.pkl','rb') as f:
    model=pickle.load(f)

# ML FLOW 
MODEL_VERSION='1.0.0'  # we got this model by model registry


# Get class label from models(important for the matching probabilites to class name 
class_labels=model.classes_.tolist()



def predict_output(user_input:dict):
    df=pd.DataFrame([user_input])


    predicted_class=model.predict(df)[0]


    # Get the probabilites for all classes
    probabilities=model.predict_proba(df)[0]
    confidence=max(probabilities)

    # Creating mapping:{classname:probabilites}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }

   
