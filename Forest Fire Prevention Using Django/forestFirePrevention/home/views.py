from django.template.response import TemplateResponse
from django.shortcuts import render
import templates
import pickle
import numpy as np
from home.models import Fire

# Create your views here.


def home(request):
    if(request.method == "POST"):
        oxygen = request.POST['oxygen']
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']



        model = pickle.load(open("model.pkl", "rb"))

        features = [int(oxygen), int(temperature), int(humidity)]
        final = [np.array(features)]

        prediction = model.predict_proba(final)
        output = '{0:.{1}f}'.format(prediction[0][1], 2)

        ins = Fire(oxygen = oxygen, temperature = temperature, humidity = humidity, output = output)
        ins.save()
        print(output)
        output = float(output)
        print(output)


        if output> 0.5:
            print('Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output))
            msg = "Your Forest is in Danger.Probability of fire occuring is "+str(output)
        elif output == 0.00 or output == 0.0 or output == 0:
            # print('Your Forest is safe.\nProbability of fire occuring is {}'.format(output))
            msg = "Your Forest is Safe.Probability of fire occuring is 0.0"
        else:
            print('Your Forest is safe.\nProbability of fire occuring is {}'.format(output))
            msg = "Your Forest is Safe.Probability of fire occuring is "+str(output)
        dict2 = {'output': output, 'msg': msg}
        return TemplateResponse(request, 'base.html', dict2)
        

        
    return render(request, 'base.html')


def predict(request):
    allPredictions = Fire.objects.all()
    context = {'predictions': allPredictions}
    return render(request, 'predictions.html', context)