data = {
    "event": ["9/11", "3/22", "4/21"],
    "orders_req_cancellation": {
        "9/11": {
            "cake": 2,
            "special_occa": {},
            "coke": 1
            },
        "3/22": {
            "coke": 2,
            "special_occa": {}            
            },
        "4/21": {
            "cake": 2,
            "special_occa": {}
            }
        },
    "form_id": {
        "9/11": {
            "input": "42718hhs",
            "output": 0
            },
        "3/22": {
            "input": 0,
            "output": 0
            },
        "4/21": {
            "input": 0,
            "output": 0
            }
        }
    }


def refresh_event_order():

    #does base checking from data['event']
    sorted_list = data['event'].copy()
    sorted_list.sort()

    copied_otf  = data['orders_tofill'].copy()
    copied_orc  = data['orders_req_cancellation'].copy()
    copied_morc = data['manual_orders_req_cancellation'].copy()
    copied_ena  = data['event_name'].copy()
    copied_fid  = data['form_id'].copy()

    data['event'] = sorted_list
    data['orders_tofill'] = {}
    data['orders_req_cancellation'] = {}
    data['manual_orders_req_cancellation'] = {}
    data['event_name'] = {}
    data['form_id'] = {}

    for i in sorted_list:
        data['orders_tofill'][i] = copied_otf[i]
        data['orders_req_cancellation'][i] = copied_orc[i]
        data['manual_orders_req_cancellation'][i] = copied_morc[i]
        data['event_name'][i] = copied_ena[i]
        data['form_id'][i] = copied_fid[i]

print(data)

refresh_event_order()

print(data)
