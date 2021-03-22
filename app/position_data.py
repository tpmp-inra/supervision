import socket
import re, json, requests


resp = requests.get(
    "https://raw.githubusercontent.com/tpmp-inra/supervision/main/positions.json"
)
camera_positions = json.loads(resp.text)
ip_list = list(camera_positions.keys())


def get_current_position():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    cp = s.getsockname()[0]
    s.close()

    for k, v in camera_positions.items():
        if k == cp:
            return v

    return {}
