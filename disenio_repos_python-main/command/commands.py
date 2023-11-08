class Command:
    def execute(self):
        pass

class start_server_comand(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.start()

class stop_server_command(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.stop()

class restart_server_command(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.restart()
