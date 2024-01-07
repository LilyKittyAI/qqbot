from datetime import datetime

import pytest
from nonebot.adapters.console import Message, MessageEvent
from nonebug import App
from nonechat.info import User


@pytest.mark.asyncio
async def test_echo(app: App):
    from qqbot.plugins.admin.plugins.bot_utils import Echo

    test_string = "test 132"

    event = MessageEvent(
        time=datetime.now(),
        self_id="test",
        message=Message(f"/echo {test_string}"),
        user=User(id=123456789),
    )
    async with app.test_matcher(Echo) as ctx:
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, test_string, result=None)
        ctx.should_finished(Echo)
