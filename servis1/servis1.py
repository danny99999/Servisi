import aiohttp
import asyncio
from aiohttp import web
from pomocneFunkcije import forwardToWT

routes = web.RouteTableDef()

@routes.get("/")

async def func(request):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            zadatak= asyncio.create_task(session.get("http://127.0.0.1:8081/"))
            response= await asyncio.gather(zadatak)
            responsePodaci= await response[0].json()

            dictPodaci= [{"id":item[0], "username":item[1], "ghlink":item[2], "content":item[3]} for item in responsePodaci.get("podaci")]
            servis2Res= await forwardToWT("http://127.0.0.1:8083/", dictPodaci)
            servis3Res= await forwardToWT("http://127.0.0.1:8084/", dictPodaci)
            return web.json_response({"naziv": "servis1", "status": "OK", "response":[servis2Res, servis3Res]}, status=200)


    except Exception as e:
        return web.json_response({"naziv": "servis1", "error": str(e)}, status=500)






app= web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8082)