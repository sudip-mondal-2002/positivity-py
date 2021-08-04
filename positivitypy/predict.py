import pickle
import os
class Predictor:
    def __init__(self, pred, transformer):
        self.pred = pred
        self.transformer = transformer
    def predict(self, text:str)->int:
        text=text.replace("n't"," not")
        ans=self.pred.predict(self.transformer.transform([text]).toarray())[0]
        if "not" in text:
            return(1-ans)
        else:
            return(ans)

def predict(text:str)->bool:
    predict_file = open(os.path.dirname(__file__)+'/predFile.pickle', 'rb')
    predict_model = pickle.load(predict_file,)
    predict_file.close()
    return predict_model.predict(text)

