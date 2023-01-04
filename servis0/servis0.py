import aiosqlite
from aiohttp import web
from helpFunkcije import dohvatRandomRedova, dodavanjeuBazu

routes= web.RouteTableDef()







app= web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8081)