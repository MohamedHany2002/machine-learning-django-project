import pickle
def prediction(user_data):
    data = [user_data]
    myfile = open('classifier','rb')
    cls=pickle.load(myfile)
    new_prediction=cls.predict(data)
    return new_prediction

# prediction([1,1,11,1,1,19,1,1])



