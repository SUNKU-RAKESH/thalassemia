from django.shortcuts import render
from django.http import HttpResponse
from joblib import load

chain_classifier = load('./savedModels/chain_classifier.joblib')


def predictor(request):
    if request.method == 'POST':
        param1 = request.POST.get('param1')
        param2 = request.POST.get('param2')
        param3 = request.POST.get('param3')
        param4 = request.POST.get('param4')
        param5 = request.POST.get('param5')
        param6 = request.POST.get('param6')
        param7 = request.POST.get('param7')
        param8 = request.POST.get('param8')
        param9 = request.POST.get('param9')
        param10 = request.POST.get('param10')

        y_pred = chain_classifier.predict(
            [[param1, param2, param3, param4, param5, param6, param7, param8, param9, param10]])
        pred = y_pred.flatten().astype(int)

        Blood_test_result = ["abnormal", "inconclusive", "normal", "slightly abnormal"]
        Genetic_Disorder = ["Mitochondrial genetic inheritence disorders",
                            "Multifactorial genetic inheritence disorders",
                            "Single-gene inheritence diseases"]
        Disorder_Subclass = ["Alzheimer's", "Cancer", "Cystic fibrosis", "Diabetes", "Hemochromatosis",
                             "Leber's hereditary optic neuropathy", "Leigh syndrome", "Mitochondrial myopathy",
                             "Tay-Sachs"]

        result1 = Blood_test_result[pred[0]]
        result2 = Genetic_Disorder[pred[1]]
        result3 = Disorder_Subclass[pred[2]]

        return render(request, 'main.html', {'result1': result1, 'result2': result2, 'result3': result3})

    return render(request, 'main.html')
