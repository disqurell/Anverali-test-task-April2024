from flask import Blueprint, request, Response
from utils.resolve_gender import check_gender
from utils.constants import NOT_DEFINED
import requests

handler = Blueprint("handler", __name__)


@handler.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    gender = check_gender(data)

    if gender == NOT_DEFINED:
        return Response(response="Gender not defined.\nCheck input data.", status=404)

    url = "https://<org_name>.bitrix24.ru/rest/1/<gen_code>/userfield.update.json"
    headers = {"Content-Type": "application/json"}

    requests.patch(
        url=url,
        headers=headers,
        json={"id": data["id"], "fields": {"GENDER": gender}},
        headers=headers,
    )

    return gender
