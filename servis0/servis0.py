import aiosqlite
import asyncio
from aiohttp import web
from pomocneFunkcije import dohvatRandomRedova, dodavanjeuBazu

routes= web.RouteTableDef()

@routes.get("/")
async def func(request):
    try:
        async with aiosqlite.connect("Servisi-database.db") as db:
            async with db.execute("SELECT COUNT(1) WHERE EXISTS (SELECT*FROM datatable)") as cursor:
                async for row in cursor:
                    if row[0]==0:
                        await dodavanjeuBazu()
                    podaci= await dohvatRandomRedova(db)
                    


        return web.json_response({"naziv": "servis0", "status": "OK", "podaci":podaci}, status=200)

    except Exception as e:
        return web.json_response({"naziv": "servis0", "error": str(e)}, status=500)           


app= web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8081)