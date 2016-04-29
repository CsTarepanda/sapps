import ws
from lib.mylib_cls import Json

class WebSocket(ws.WebSocket):
    URL = r"/chat/$"

    def on_message(self, message):
        WebSocket.all_send_message(Json(
            username=self.username,
            message=message,
            ))
