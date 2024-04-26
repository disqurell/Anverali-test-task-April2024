from db.database import db
from .constants import MALE, FEMALE, NOT_DEFINED


def check_gender(data: dict):
    contact_id = data.get("ID", None)
    contact_name = data.get("name", None)

    gender = None

    if (contact_id or contact_name) is None:
        return None

    from_woman_table = db.select_from_table_with_condition(
        "names_woman", contact_name, contact_id
    )
    from_man_table = db.select_from_table_with_condition(
        "names_man", contact_name, contact_id
    )

    db.close_connection()

    if from_woman_table:
        gender = FEMALE
    elif from_man_table:
        gender = MALE
    else:
        gender = NOT_DEFINED

    return gender
