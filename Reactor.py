from twisted.internet import reactor


def explode(message):
    print('BOOM! ') + message


reactor.callLater(1, explode, 'first one')
reactor.callLater(2, explode, 'second one')
reactor.callLater(3, reactor.stop)
reactor.run()
