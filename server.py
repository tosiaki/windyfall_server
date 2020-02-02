from aiohttp import web
import socketio

app = web.Application()
sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
sio.attach(app)

@sio.event
def connect(sid, environ):
    print(f'Connection from {environ["REMOTE_ADDR"]}')
    print(sid)

if __name__ == '__main__':
    web.run_app(app)
