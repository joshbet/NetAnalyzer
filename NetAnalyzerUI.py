"""This script starts and displays the NetAnalyzer GUI.
Matthew Wells, 2021
"""


from tg import expose, TGController, MinimalApplicationConfigurator
from wsgiref.simple_server import make_server
from NMapScan import main as portScan
import webbrowser

class RootController(TGController):
    """This class exposes interfaces on localhost:8080. Each exposed function
    can be accessed by an http call to localhost:8080/identifier, where
    identifier is the name of the exposed function. Arguments are passed
    as normal for http calls, in the format ?paramater_name=value.
    """
    @expose('NetAnalyzer.xhtml')
    def NetAnalyzer(self, ip=None):
        if (ip):
            print('Opening IP ' + ip)
            if (ip == '127.0.0.1'):
                device_name = "This computer"
            else:
                device_name = ip
            try:
                vulnerabilities = portScan(ip)
            except KeyError:
                vulnerabilities = []
                device_name = 'Invalid IP Address'
            solutions = {}
            for vulnerability in vulnerabilities:
                solutions[vulnerability] = "..."
            return dict(vulnerabilities=vulnerabilities, solutions=solutions, device_name=device_name)
        else:
            vulnerabilities = []
            solutions = []
            device_name = ''
            return dict(vulnerabilities=vulnerabilities, solutions=solutions, device_name=device_name)

config = MinimalApplicationConfigurator()
config.update_blueprint({
    'root_controller': RootController(),
    'renderers': ['kajiki']
})

application = config.make_wsgi_app()

print("Serving on port 8080...")
httpd = make_server('', 8080, application)
webbrowser.open('http://localhost:8080/NetAnalyzer?ip=127.0.0.1')
httpd.serve_forever()
