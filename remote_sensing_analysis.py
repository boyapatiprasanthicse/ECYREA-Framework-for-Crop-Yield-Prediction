import numpy as np
from tensorflow.keras.models import load_model

def analyze_image(image):
    model = load_model('crop_health_model.h5')
    prediction = model.predict(np.expand_dims(image, axis=0))
    return prediction
