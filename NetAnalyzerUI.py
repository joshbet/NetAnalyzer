from tg import expose, TGController, MinimalApplicationConfigurator
from wsgiref.simple_server import make_server
from Script1 import main as portScan

class RootController(TGController):
    @expose()
    def index(self):
        return 'Hello World!'

    @expose('mockup_one.xhtml')
    def NetAnalyzer(self):
        vulnerabilities = portScan()
        solutions = {}
        for vulnerability in vulnerabilities:
            solutions[vulnerability] = "..."
        return dict(vulnerabilities=vulnerabilities, solutions=solutions)

config = MinimalApplicationConfigurator()
config.update_blueprint({
    'root_controller': RootController(),
    'renderers': ['kajiki']
})

application = config.make_wsgi_app()

print("Serving on port 8080...")
httpd = make_server('', 8080, application)
httpd.serve_forever()
