import aiohttp

async def SlanjeNaServis4(podaci):
	async with aiohttp.ClientSession(connector = aiohttp.TCPConnector(ssl = False)) as session:
		async with session.post("http://servis4:8085/skupljanjePodataka", json = podaci) as response:
			service4Res = await response.json()
	return service4Res