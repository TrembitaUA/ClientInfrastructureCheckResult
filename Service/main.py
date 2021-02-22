from spyne.server.wsgi import WsgiApplication
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from apps import spyned
from apps.flasked import app

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {'/CIC': WsgiApplication(spyned.create_app(app))}
)

if __name__ == '__main__':
    app.run(threaded=True)
