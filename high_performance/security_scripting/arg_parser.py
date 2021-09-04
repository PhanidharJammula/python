import argparse, socket

parser = argparse.ArgumentParser(description="this is the description")
parser.add_argument('--listen-port', type=int, help="Listen Address")
parser.add_argument('--backdoor-port', type=int, help="Optional")

cmd_args = parser.parse_args()

var = cmd_args.listen_port
var1 = cmd_args.backdoor_port
print(var, var1)
print(socket.getfqdn())
print(socket.gethostbyname(socket.getfqdn()))