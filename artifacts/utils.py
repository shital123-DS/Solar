
import numpy as np
import pickle

class solar():

    def __init__(self,data):
        self.data = data

    def load_model(self):
        with open(r'artifacts/model.pkl','rb') as file:
            self.model = pickle.load(file)

    def predict(self):
        self.load_model()

        Pmax = float(self.data['Pmax'])
        Vmp = float(self.data['Vmp'])
        Imp = float(self.data['Imp'])
        Voc = float(self.data['Voc'])
        Isc = float(self.data['Isc'])

        input1 = np.array([Pmax,Vmp,Imp,Voc,Isc], ndmin=2)

        solar_pred = self.model.predict(input1)[0]
        print(f'Solar Panel Efficiency Prediction : {solar_pred}')
        return solar_pred

if __name__ == "__main__":
    
    Pmax = 590.00
    Vmp = 44.91
    Imp = 13.14
    Voc = 54.76
    Isc = 13.71

    input1 = np.array([Pmax,Vmp,Imp,Voc,Isc], ndmin=2)

    solar_obj = solar(input1,Pmax,Vmp,Imp,Voc,Isc)
    solar_obj.predict()