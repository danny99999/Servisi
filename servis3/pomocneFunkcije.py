import aiohttp

async def slanjeNaServis4(podaci):
	async with aiohttp.ClientSession(connector = aiohttp.TCPConnector(ssl = False)) as session:
		async with session.post("http://servis4:8085/skupljanjePodataka", json = podaci) as response:
			servis4Res = await response.json()

	return servis4Res
