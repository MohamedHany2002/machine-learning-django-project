from django.shortcuts import render
# from ml_model import titanic
from ml_model.titanic import prediction
# Create your views here.

def home(request):
    data_list = []
    if request.GET:
        data_list.append(int(request.GET.get('Pclass')))
        data_list.append(int(request.GET.get('Sex')))
        data_list.append(int(request.GET.get('Age')))
        data_list.append(int(request.GET.get('SibSp')))
        data_list.append(int(request.GET.get('Parch')))
        data_list.append(int(request.GET.get('Fare')))
        data_list.append(int(request.GET.get('Embarked')))
        data_list.append(int(request.GET.get('Title')))
        new_prediction=prediction(data_list)
        print(type(new_prediction))
        if new_prediction==1:
            result= 'Survived'
        else:
            result='not survived'
        return render(request,"home.html",{'prediction':result})
    else:
        return render(request,"home.html")





# ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare','Embarked', 'Title']