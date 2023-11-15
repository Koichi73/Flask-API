from flask import Blueprint, render_template, request, redirect, jsonify
from flask_app import db
from flask_app.models import Stocks
from sqlalchemy import func
from flask_app.views import input_check

stocks_bp = Blueprint("stocks", __name__, url_prefix="/stocks")


@stocks_bp.route("/", methods=["GET", "POST", "DELETE"], strict_slashes=False)
def stocks():
    # 在庫の追加
    if request.method == "POST":
        # 入力値の取得・確認
        input_json = request.get_json()
        if input_check.input_check(input_json) == False:
            return jsonify({"message": "INPUT_ERROR"}) # 入力エラーを表示
        name, amount = input_json["name"], input_json["amount"]

        # DBに追加
        stocks = Stocks(name=name, amount=amount)
        db.session.add(stocks)
        db.session.commit()

        # response設定
        new_location = (request.url + name) 
        response = redirect(new_location, code=302)
        response.data = jsonify(input_json).data
        return response
    
    # 在庫の全削除
    elif request.method == "DELETE":
        db.session.query(Stocks).delete()
        db.session.commit()
        return "DELETED"
    
    # 全ての在庫の表示
    else:
        total_amount_list = db.session.query(Stocks.name, func.sum(Stocks.amount)) \
                                .group_by(Stocks.name) \
                                .having(func.sum(Stocks.amount) != 0) \
                                .all()
        if len(total_amount_list) == 0:
            return jsonify({"message": "NO STOCKS"}) # 在庫がないことを表示
        else:
            json_data = {item[0]: item[1] for item in total_amount_list}
            return jsonify(json_data)


@stocks_bp.route("/<name>", methods=["GET", "POST"], strict_slashes=False)
def stocks_name(name):
    total_amount = db.session.query(func.sum(Stocks.amount)) \
                                .filter(Stocks.name == name) \
                                .scalar()
    
    if total_amount != None:
        output_json = {name: total_amount}
    else:
        output_json = {name: 0}

    return jsonify(output_json)