from pyhooked import Hook,KeyboardEvent,MouseEvent

def handle_events(args):
    if isinstance(args,KeyboardEvent):
        print(args.key_code,args.current_key,args.event_type)
    if isinstance(args,MouseEvent):
        print(args.mouse_x,args.mouse_y)

hk=Hook()
hk.handler=handle_events
hk.hook()
