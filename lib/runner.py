import os, subprocess

class Runner:
    def __init__(self, executable, path, add_shell):
        self.executable = executable.copy()
        self.path = path
        self.params = []
        self.add_shell = add_shell
    def addStartup(self, runner):
        self.startup.append(runner)
    def setStartup(self, runner):
        self.startup = []
        self.startup.append(runner)
    def setParams(self, params):
        self.params = params.copy()
    def addParam(self, param):
        self.params.append(param)
    def setExecutable(self, executable):
        self.executable = executable.copy()
    def addExecutable(self, executable):
        self.executable.append(executable)
    def setPath(self, path):
        self.path = path
    def run(self):
        path = self.path
        call = self.executable.copy()
        if self.params:
            for index, param in enumerate(self.params):
                call.append(param)
        if self.add_shell:
            result = subprocess.run(call, cwd=path, capture_output=True, shell=True, check=True)
        else:
            result = subprocess.run(call, cwd=path, capture_output=True)
        return result

    def runStartup(self):
        if self.runners:
            for index, runner in enumerate(self.startup):
                runner.run()
