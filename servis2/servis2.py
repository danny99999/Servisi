from aiohttp import web
from pomocneFunkcije import SlanjeNaServis4

responses = []
routes = web.RouteTableDef()

@routes.post("/")
async def func(request):
	global responses
	print("here")
	try:
		responseData = await request.json()

		if responseData.get("username").lower().startswith("w"):
			response = await SlanjeNaServis4(responseData)
			responses.append(response)
		
		return web.json_response({"naziv": "servis2", "status": "OK", "servis4 responses": responses}, status = 200)

	except Exception as e:
		return web.json_response({"naziv": "servis3", "error": str(e)}, status = 500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8083)
