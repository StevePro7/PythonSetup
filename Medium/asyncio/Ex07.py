import asyncio
import aiofiles

async def read_file_async(filepath):
    async with aiofiles.open(filepath, 'r') as file:
        return await file.read()


async def read_all_async(filepaths):
    tasks = [read_file_async(filepath) for filepath in filepaths]
    return await asyncio.gather(*tasks)

async def main():
    filepaths = ['file1.txt', 'file2.txt']
    data = await read_all_async(filepaths)
    print(data)


asyncio.run(main())