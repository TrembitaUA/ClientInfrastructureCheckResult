from datetime import datetime

from spyne import DateTime, rpc, Application, Service, ComplexModel
from spyne.protocol.soap import Soap11


class Response(ComplexModel):
    __namespace__ = 'https://trembita.gov.ua/'
    __type_name__ = 'Response'
    ReceivedTime = DateTime(doc='Отриманий час', min_occurs=1)
    GeneratedTime = DateTime(doc='Згенерований час', min_occurs=1)


class CIC(Service):
    @rpc(DateTime(doc='Надайте час', min_occurs=1),
         _returns=Response)
    def ClientInfrastructureCheck(ctx, DateTimeSend):
        R = Response()
        R.ReceivedTime = DateTimeSend
        R.GeneratedTime = datetime.now()
        return R


class UserDefinedContext(object):
    def __init__(self, flask_config):
        self.config = flask_config


def create_app(flask_app):
    application = Application(
        [CIC],
        tns='https://trembita.gov.ua/',
        name='ClientInfrastructureCheck',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )

    def _flask_config_context(ctx):
        ctx.udc = UserDefinedContext(flask_app.config)

    application.event_manager.add_listener('method_call', _flask_config_context)

    return application
