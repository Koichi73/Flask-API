# 入力値(json)が条件を満たしているか確認する
def input_check(json_data):
    result = True
    
    # nameキーの条件
    if "name" in json_data:
        name = json_data["name"]
        if not (len(name) <= 8 and name.isalpha()):
            result = False
    else:
        result = False
    
    # amountキーの条件
    if "amount" in json_data:
        amount = json_data["amount"]
        if not (isinstance(amount, int) and amount > 0):
            result = False
    else:
        result = False

    return result