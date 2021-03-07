from json import dumps
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def rules(request):
    return render(request, 'myapp/rules.html')


@csrf_exempt
def Parameters(request):

    rule_name = request.POST.get('rule_name')
    country = request.POST.get('country')
    state = request.POST.get('state')
    region = request.POST.get('region')
    group_id = request.POST.get('group_id')
    device_id = request.POST.get('device_id')
    status = request.POST.get('status')
    res_name = request.POST.get('res_name')
    operator = request.POST.get('operator')
    resource_value = request.POST.get('resource_value')
    fault_type = request.POST.get('fault_type')
    event_name = request.POST.get('event_name')
    action_type = request.POST.get('action_type')
    emails = request.POST.get('emails')
    subject = request.POST.get('subject')
    email_content = request.POST.get('email_content')

    payload = {'rule_name': rule_name, 'country': country, 'state': state , 'region': region, 'group_id': group_id, 'device_id': device_id,
    'status': status, 'res_name': res_name, 'operator': operator, 'resource_value': resource_value, 'fault_type': fault_type, 'event_name': event_name, 'action_type': action_type, 'emails': emails, 'subject': subject, 'email_content': email_content}

    response = requests.post('http://127.0.0.1:5000/param', json=payload)

    print('Status Code: ', response.status_code)
    print('data: ', response.json())

    if response.status_code == 200:
        print("success")
    else:
        print("Error Occured !")

    datajson = dumps(payload)
    return render(request, 'myapp/rules.html', {'data': datajson})
