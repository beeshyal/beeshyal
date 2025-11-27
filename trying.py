import subprocess

# Read password from file
with open("clb.txt", "r") as f:
    wifi_password = f.read().strip()

wifi_name = "sumnima56_fpkhr"

# Connect using nmcli
command = ["nmcli", "dev", "wifi", "connect", wifi_name, "password", wifi_password]

try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    print("Connected Successfully!")
    print(output.decode())
except subprocess.CalledProcessError as e:
    print("Connection Failed!")
    print(e.output.decode())