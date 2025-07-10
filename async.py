import time
words = [
'gegege',
'bebebe',
'azaza',
'pipipi',
'yayayayya',
'zxc',
'qwer',
'wasd',
'qwerasddfgzxcvn '
'end'
]

for word in words:
    print(word)
    time.sleep(1)




import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f'{name} after {delay} seconds!')

async def main():
    await asyncio.gather(
        say_hello('прив', 2),
        say_hello('пивет', 3),
        say_hello('пр', 0.5),
        say_hello('приверттттт', 8),
        say_hello('ппппппппппппррррррррррррррииииииииииииииииииииииввввввввввввввввввеееееееееет', 25)
    )
    print('end')

asyncio.run(main())
