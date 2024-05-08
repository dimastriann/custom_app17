import xmlrpc.client
import json
import requests


odoo_url = "http://127.0.0.1:8047"
odoo_user = "admin"
odoo_pass = "admin"
odoo_db = "v17_dev_training"


def test_xml_rpc():
    # logging in
    common = xmlrpc.client.ServerProxy(f"{odoo_url}/xmlrpc/2/common")
    print(common.version())
    uid = common.authenticate(odoo_db, odoo_user, odoo_pass, {})

    # call methods
    obj = xmlrpc.client.ServerProxy(f"{odoo_url}/xmlrpc/2/object")
    record = obj.execute_kw(odoo_db, uid, odoo_pass, "sale.order", "create", [[["name", '=', "S00003", ["date_order"]]]])
    rec_result = obj.execute_kw(odoo_db, uid, odoo_pass, "sale.order", "read", [record, ["name", "partner_id", "amount_total"]])
    print(record)
    print(rec_result)
    # custom code


# test_xml_rpc()


def test_json_rpc(model_name=False, method_name=False, args=False, params=False):
    # logging in
    data = {
        "jsonrpc": "2.0",
        "params": {
            "db": odoo_db,
            "login": odoo_user,
            "password": odoo_pass
        }
    }
    data = json.dumps(data).encode()
    rpc_response = requests.post(
        url=f'{odoo_url}/web/session/authenticate',
        data=data,
        headers={
            "Content-Type": "application/json",
        }
    )
    res_response = rpc_response.json()
    print("auth", rpc_response)

    data = {
        "jsonrpc": "2.0",
        "params": {
            "model": "res.partner",
            "method": "search",
            "args": [[["is_company", '=', True]]],
            "kwargs": {}
        }
    }
    # cookies = dict(session_id=res_response['result'].get('session_id', False))
    call_response = requests.post(
        url=f'{odoo_url}/web/dataset/call_kw',
        data=json.dumps(data).encode(),
        cookies=dict(session_id=rpc_response.cookies.get('session_id')),
        headers={
            "Content-Type": "application/json",
        }
    )

    data = {
        "jsonrpc": "2.0",
        "params": {
            "model": "res.partner",
            "method": "create",
            "args": [[{"name": "dimas"}]],
            "kwargs": {}
        }
    }

    call_response = requests.post(
        url=f'{odoo_url}/web/dataset/call_kw',
        data=json.dumps(data).encode(),
        cookies=dict(session_id=rpc_response.cookies.get('session_id')),
        headers={
            "Content-Type": "application/json",
        }
    )
    call_result = call_response.json()
    print("call", call_result)


test_json_rpc()
