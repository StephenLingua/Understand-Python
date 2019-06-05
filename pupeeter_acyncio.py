# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pupeeter_acyncio
   Description：
   Author :       stephen
   date：          2019/6/4
-------------------------------------------------
   Change Activity:
                   2019/6/4:
-------------------------------------------------
"""
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({'dumpio':True, 'headless': False})
    page = await browser.newPage()
    await page.goto('http://google.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

# 测试，正常打开
