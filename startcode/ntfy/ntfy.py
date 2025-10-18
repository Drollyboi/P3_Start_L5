chatName = "Cheese"

import requests

requests.post(f"https://ntfy.sh/{chatName}",
    data="Remote access to phils-laptop detected. Act right away.",
    headers={
        "Title": "Unauthorized access detected",
        "Priority": "urgent",
        "Tags": "warning,skull"
    })
