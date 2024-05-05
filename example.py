import time 
import numpy as np 
import asyncio

async def get_squares(n:float)->float:
    """
    Gets square of a given number
    """
    await asyncio.sleep(1)
    return n**2

async def main():
    t1 = time.time()
    print('Program Started')
    a = np.random.normal(loc=10, scale=1, size=1000)
    tasks = []
    for i in a:
        tasks.append(asyncio.create_task(get_squares(i)))
    b = await asyncio.gather(*tasks)
    print(b)
    print('Done!')
    t2 = time.time()
    print(f'Time required to complete the task : {(t2-t1):.2f} s')

if __name__=='__main__':
    asyncio.run(main())