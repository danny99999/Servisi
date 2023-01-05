import pathlib
import aiofiles
from aiohttp import web

primljenKod= []

routes= web.RouteTableDef()

@routes.post("/skupljanjePodataka")
async def func(request):
    global primljenKod
    try:
        podaci= await request.json()
        primljenKod.append({"username": podaci.get("username"), "sadržaj": podaci.get("sadržaj")})

        if len(primljenKod) > 10:
            pathlib.Path("files").mkdir(parents=True, exist_ok=True)
            for item in primljenKod:
                async with aiofiles.open("files%s.txt"%(item.get("username")), "w") as writer:
                    await writer.write(item.get("sadržaj"))
            primljenKod.clear()
        return web.json_response({"naziv": "servis4", "status": "OK"}, status = 200)    



    except Exception as e:
        return web.json_response({"naziv": "servis4", "error": str(e)}, status = 500)



app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port = 8085)