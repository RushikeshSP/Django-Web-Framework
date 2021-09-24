from django.shortcuts import render
import templates
import pickle
import numpy as np

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

        if output>str(0.5):
            print('Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output))
        else:
            print('Your Forest is safe.\n Probability of fire occuring is {}'.format(output))

        # context = {'oxygen': oxygen, 'temperature': temperature, 'humidity': humidity, 'output': output}
        # return render(request, 'base.html', context)

    return render(request, 'base.html')


def predict(request):
    return render(request, 'predictions.html')