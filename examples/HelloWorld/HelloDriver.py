#!/usr/bin/python

from CCAPython.framework.manage.builders import FrameworkHandle
from CCAPython.gov.cca.ports import GoPort

if __name__ == '__main__':
  fwk = FrameworkHandle()
  
  server = fwk.createInstance("HelloServerInstance", "HelloServer.Component", None )
  client = dec.createInstance("HelloClientInstance", "HelloClient.Component", None )
  fwk.connect(client, "HelloServer", server, "HelloServer")

  goport = fwk.lookupPort(client, "GoPort")
  goport.go()

  fwk.destroyInstance(server,0.0)
  fwk.destroyInstance(client,0.0)
