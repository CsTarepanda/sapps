import ws
from ws import route
from lib.mylib_cls import Json

@route()
class ChatServer(ws.WebSocket, ws.Router):
    BASE_URL = ws.Router.plus("chat")

    def on_message(self, message):
        ChatServer.all_send_message(Json(
            username=self.username,
            message=message,
            ))
