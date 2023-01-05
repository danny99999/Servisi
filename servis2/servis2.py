from aiohttp import web
from pomocneFunkcije import SlanjeNaServis4

odgovori = []
routes = web.RouteTableDef()

@routes.post("/")
async def func(request):
	global odgovori
	print("here")
	try:
		responsePodaci = await request.json()

		if responsePodaci.get("username").lower().startswith("w"):
			odgovor = await SlanjeNaServis4(responsePodaci)
			odgovori.append(odgovor)
		
		return web.json_response({"naziv": "servis2", "status": "OK", "servis4 odgovori": odgovori}, status = 200)

	except Exception as e:
		return web.json_response({"naziv": "servis3", "error": str(e)}, status = 500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8083)
