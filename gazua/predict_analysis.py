from django.conf import settings
import numpy as np
import joblib



def predict_stock(data_1d_array):

    base_url = settings.MEDIA_ROOT_URL + settings.MEDIA_URL # == './media/'
    model_url = base_url + 'model.joblib'
    model_loaded = joblib.load(model_url)
    # ex) [5.8, 2.8, 5.1, 2.4] -> array([[5.8, 2.8, 5.1, 2.4]])
    data_2d_array = np.reshape(data_1d_array, (1, 16))
    result_class = model_loaded.predict(data_2d_array) # ex) array([2])
    result_class = result_class[0] # predicted class, ex) 2

    target_names = ['주가_상승', '주가_하락']
    predict_result = target_names[result_class]

    return predict_result
