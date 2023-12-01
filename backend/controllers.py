import joblib

def predict(arr):
    model = joblib.load('utils/Erythemato-Squamous-Disease.joblib')
    prediction = model.predict([arr])[0]

    stage = {
        0: 'negative',
        1: 'primary stage 1',
        2: 'primary stage 2',
        3: 'DANGER APPROACHING 1',
        4: 'DANGER APPROACHING 2',
        5: 'critical. you died'
    }
    return stage[prediction]

def result(patient_info):
    patient_info['result'] = predict(patient_info['symptoms'])
    
    return patient_info