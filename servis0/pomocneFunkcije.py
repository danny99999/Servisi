import aiosqlite
import numpy as np
import pandas as pd

async def dohvatRandomRedova(connection):
    cursor= await connection.cursor()
    await cursor.execute("SELECT COUNT (*) FROM datatable")
    (brRedova, )= await cursor.fetchone()
    randRowIndices= np.random.randint(0, brRedova, size= 100)

    redovi= []
    for rowIndex in randRowIndices:
        await cursor.execute("SELECT * FROM datatable LIMIT 1 OFFSET %s"%(rowIndex))
        redovi.append(await cursor.fetchone())
    return redovi

async def dodavanjeuBazu():
    try:
        dataframe= pd.read_json('servis0/podaci/dataset.json', lines=True)
        async with aiosqlite.connect("Servisi-database.db") as db:
            for index, row in dataframe.head(10000).iterrows():
                await db.execute("INSERT INTO datatable(username, ghlink, filename, content) VALUES (?,?,?,?)", 
                (row.get("repo_name").split("/")[0],
                "https://github.com/%s"%(row.get("repo_name")),
                row.get("path").split("/")[-1],
                row.get("content")))
                await db.commit()
        print("Uspješno dodavanje podataka u bazu.")

    except Exception as e:
        print("Pojavila se greška kod dodavanja podataka u bazu iz dataseta:", e)           
    pass    