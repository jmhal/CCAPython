#!/usr/bin/python

from framework.manage.builders import FrameworkHandle
#from gov.cca.ports import GoPort

if __name__ == '__main__':
  fwk = FrameworkHandle()
  
  server = fwk.createInstance("HelloServerInstance", "examples.HelloWorld.HelloServer.Component", None)
  client = fwk.createInstance("HelloClientInstance", "examples.HelloWorld.HelloClient.Component", None)
 
  fwk.connect(client, "HelloServer", server, "HelloServer")

  
  goport = fwk.lookupPort(client, "GoPort")
  goport.go()
  
  fwk.destroyInstance(server, 0.0)
  fwk.destroyInstance(client, 0.0)
 
