import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    g = asyncio.gather(count(), count(), count())
    print(g)
    await g    

import time
s = time.perf_counter()

#loop = asyncio.get_event_loop()
#f = asyncio.gather(main())
#print(type(f))
#loop.run_until_complete(f)


#asyncio.run(main())


#t = asyncio.ensure_future(main())
#loop = asyncio.get_event_loop()
#loop.run_until_complete(t)


#This does not work 
#loop = asyncio.get_event_loop().run_forever()
#loop.create_task(main())
#loop.close()

#This does 
#loop = asyncio.get_event_loop()
#t=loop.create_task(main())
#print(type(t))
#loop.run_until_complete(t)

loop = asyncio.get_event_loop()
t=asyncio.ensure_future(main())
loop.run_until_complete(t)

elapsed = time.perf_counter() - s
print(f"{__file__} executed in {elapsed:0.2f} seconds.")