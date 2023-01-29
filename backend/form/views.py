from django.shortcuts import render
from django.http import HttpResponse
from .forms import Form
from transactions.models import Transaction


def home(request):
    formModel = Form()
    return render(request, "home.html", {"form": formModel})


def data_response(request):
    # getting form response
    formResponse = Form(request.POST)
    codeData = formResponse.data["code"]
    # making a list
    codeDataList = list(codeData)
    # separating the code

    # getting transaction number
    def getTransaction():
        transactionNumber = codeData[0]
        if transactionNumber == "2" or "3" or "9":
            return "Saida"
        else:
            return "Entrada"

    transactionType = getTransaction()

    # getting date and treating it
    year = codeDataList[1:5]
    year_treated = "".join([str(elem) for elem in year])
    month = codeDataList[5:7]
    month_treated = "".join([str(elem) for elem in month])
    day = codeDataList[7:9]
    day_treated = "".join([str(elem) for elem in day])
    date = f"{year_treated}-{month_treated}-{day_treated}"

    # getting value and treating it

    value = codeDataList[9:19]
    value_to_string = "".join([str(elem) for elem in value])
    value_to_int = int(value_to_string)
    value_treated = value_to_int / 100

    # getting cpf and treating it

    cpf = codeDataList[19:30]
    cpf_to_string = "".join([str(elem) for elem in cpf])

    # getting card and treating it
    card = codeDataList[30:42]
    card_to_string = "".join([str(elem) for elem in card])

    # getting time and treating it
    hour = codeDataList[42:44]
    hour_treated = "".join([str(elem) for elem in hour])
    minutes = codeDataList[44:46]
    minutes_treated = "".join([str(elem) for elem in minutes])
    seconds = codeDataList[46:48]
    seconds_treated = "".join([str(elem) for elem in seconds])

    time = f"{hour_treated}:{minutes_treated}:{seconds_treated}"

    # getting owner and treating it
    owner = codeDataList[48:62]
    owner_to_string = "".join([str(elem) for elem in owner])

    # getting store_name and treating it
    store_name = codeDataList[62:81]
    store_name_to_string = "".join([str(elem) for elem in store_name])

    data = {
        "type": transactionType,
        "date": date,
        "value": value_treated,
        "cpf": cpf_to_string,
        "card": card_to_string,
        "hour": time,
        "store_owner": owner_to_string,
        "store_name": store_name_to_string,
    }

    form2 = Form(data)
    database2 = Transaction.objects.get(id=1).store_name
    print(database2)

    if form2.is_valid():
        form2.save()

    return render(
        request,
        "response.html",
        {"formResult": data},
    )
