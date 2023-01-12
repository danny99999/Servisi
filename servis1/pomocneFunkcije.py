import aiohttp


async def forwardToWT(WTURL, podaci):
    for index in range(len(podaci)):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(WTURL, json= podaci[index]) as response:
                WTResponse= await response.json()
    return WTResponse