from django.shortcuts import render
import requests

def getdata():
    open_file = open("chartapp/adresses.txt", "r")
    file_lines = open_file.readlines()
    first_line = file_lines[0].strip()
    second_line = file_lines[1].strip()
    third_line = file_lines[2].strip()
    fourth_line = file_lines[3].strip()
    fifth_line = file_lines[4].strip()
    first_addresses = first_line.split(',')
    second_addresses = second_line.split(',')
    third_addresses = third_line.split(',')
    fourth_addresses = fourth_line.split(',')
    fifth_addresses = fifth_line.split(',')
    addresses = [first_addresses, second_addresses, third_addresses, fourth_addresses, fifth_addresses]
    addressList = []
    for x in range(0, 5):
        for y in range(0, 20):
            addressList.append(addresses[x][y])
    urls = [
        "https://api.etherscan.io/api?module=account&action=balancemulti&address=" + first_line + "&tag=latest&apikey=YEZ2MKHZ9K7RDI2EI3I9SQ5R7KR6389FC4",
        "https://api.etherscan.io/api?module=account&action=balancemulti&address=" + second_line + "&tag=latest&apikey=YEZ2MKHZ9K7RDI2EI3I9SQ5R7KR6389FC4",
        "https://api.etherscan.io/api?module=account&action=balancemulti&address=" + third_line + "&tag=latest&apikey=YEZ2MKHZ9K7RDI2EI3I9SQ5R7KR6389FC4",
        "https://api.etherscan.io/api?module=account&action=balancemulti&address=" + fourth_line + "&tag=latest&apikey=YEZ2MKHZ9K7RDI2EI3I9SQ5R7KR6389FC4",
        "https://api.etherscan.io/api?module=account&action=balancemulti&address=" + fifth_line + "&tag=latest&apikey=YEZ2MKHZ9K7RDI2EI3I9SQ5R7KR6389FC4"]
    values = []
    accounts = []
    for x in range(0, 5):
        response = requests.get(urls[x])
        address = response.json()
        result = address.get("result")
        for obj in result:
            balance = obj.get("balance")
            values.append(int(int(balance) / (10 ** 18)))
        for i in range(1, len(values)):
            key = values[i]
            j = i - 1
            while j >= 0 and key > values[j]:
                values[j + 1] = values[j]
                addressList[j+1] = addressList[j]
                j -= 1
            values[j + 1] = key
    for x in range(1, 101):
        accounts.append(x)
    context = {
        "balances": values,
        "accounts": accounts,
        "addresses": addressList
    }
    open_file.close()
    return context, addressList
def index (request):
    return render(request, 'chartapp/index.html',getdata()[0])


def piechart(request):
    return render(request, 'chartapp/pie.html', getdata()[0])


def linegraph(request):
    return render(request, 'chartapp/line.html', getdata()[0])





