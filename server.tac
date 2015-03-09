from twisted.application.internet import SSLServer
from twisted.application.service import Application
from twisted.internet import ssl
from twisted.python.filepath import FilePath
from twisted.web.resource import Resource
from twisted.web.server import Site


fileRoot = FilePath(__file__).parent()

with fileRoot.child('server.pem').open() as infile:
    serverCert = ssl.PrivateCertificate.loadPEM(infile.read())

sslContextFactory = serverCert.options()

root = Resource()
site = Site(root)

application = Application('test')
SSLServer(5443, site, sslContextFactory).setServiceParent(application)
