import socket
import json

ip_list = ["192.168.0.22", "192.168.0.23"]

camera_positions = {
    ip_list[0]: {
        "name": "Position 1",
        "location": "Salon",
        "ip_adress": ip_list[0],
    },
    ip_list[1]: {
        "name": "Position 2",
        "location": "Cuisine",
        "ip_adress": ip_list[1],
    },
}

with open("data.txt", "w") as outfile:
    json.dump(camera_positions, outfile)


def get_current_position():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    cp = s.getsockname()[0]
    s.close()

    for k, v in camera_positions.items():
        if k == cp:
            return v

    return {}
