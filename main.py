from playwright.sync_api import sync_playwright, Response
import utils
import Model.message_pb2 as message_pb2


def response(resp: Response):
    if "https://live.douyin.com/webcast/im/fetch/" in resp.url:
        response = message_pb2.Response()
        response.ParseFromString(resp.body())
        utils.decodeMsg(response.messages)


browsers = sync_playwright().start().chromium.launch(headless=True)
page = browsers.new_page()
page.on("response", response)
page.goto(
    "https://live.douyin.com/296295439179",
)
while True:
    page.wait_for_timeout(1000)
