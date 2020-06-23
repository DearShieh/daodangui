class global_var:
    ID = 0
    run = 4
    url = 5
    method = 6
    headers = 7
    request_data = 9
    expect = 10
    result = 11

    # 获取ID
def get_id():
    return global_var.ID

    # 获取url
def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_method():
    return global_var.method

def get_headers():
    return global_var.headers

def get_headers_value():
    header = {"hasattr": "123"}

def get_request_data():
    return global_var.request_data

def get_expect():
    return global_var.expect

def get_result():
    return global_var.result