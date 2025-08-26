from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

TOPOS = {'mytopo' : (lambda : mytopo(4))}

class mytopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=4):
        switch = self.addSwitch('s1')

        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def Q1_a():
    "Create and test a simple network"
    topo = mytopo(n=4)
    net = Mininet(topo)