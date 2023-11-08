from commands import start_server_comand, stop_server_command, restart_server_command
from server import Server
from rc import RemoteControl

server = Server()
start_command = start_server_comand(server)
stop_command = stop_server_command(server)
restart_command = restart_server_command(server)
remote = RemoteControl()

remote.set_command(start_command)
remote.press_button()

remote.set_command(stop_command)
remote.press_button()

remote.set_command(restart_command)
remote.press_button()
