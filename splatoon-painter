from concurrent.futures import ThreadPoolExecutor
import nxbt
import cv2
import argparse
import asyncio
import os

from aioconsole import aprint, ainput
import functools


async def main(args, loop):
    # Create a new thread pool
    executor = ThreadPoolExecutor()

    # Create a new Controller and connect to the Switch
    nx = nxbt.Nxbt()
    if (args.reconnect):
        controller_index = await loop.run_in_executor(executor, functools.partial(nx.create_controller, nxbt.PRO_CONTROLLER,
                                                                                  reconnect_address=nx.get_switch_addresses()))
    else:
        controller_index = await loop.run_in_executor(executor, nx.create_controller, nxbt.PRO_CONTROLLER)
    await loop.run_in_executor(executor, nx.wait_for_connection, controller_index)

    await ainput('Successfully connected, please make sure the Nintendo Switch has Splatoon3 doodle page open and the brush is minimized to the top left corner. Press <Enter> to continue...')

    # Read the .bmp image file
    img = cv2.imread(args.filename, cv2.IMREAD_GRAYSCALE)
    if img.shape not in ((120, 320), (320, 120)):
        raise ValueError('The image must be 320px * 120px or 120px * 320px!')

    # Read the archieve file
    try:
        with open('.splatoon-painter.archieve', 'r') as f:
            start = list(map(int, f.read().split()))
        ans = await ainput(
            'A previous drawing record is detected, start from the previous position?(Y/n):')
        if ans in ('N', 'n', 'No', 'no'):
            start = [0, 0]
    except:
        start = [0, 0]

    user_input = asyncio.ensure_future(
        ainput('Painting... Press<Enter> to stop.')
    )

    # Locate to the former location
    for i in range(start[0]):
        await loop.run_in_executor(executor, nx.press_buttons, controller_index, [nxbt.Buttons.DPAD_DOWN])
    for i in range(start[1]):
        await loop.run_in_executor(executor, nx.press_buttons, controller_index, [nxbt.Buttons.DPAD_RIGHT])

    # Painting
    for i in range(start[0], img.shape[0]):
        for j in range(start[1], img.shape[1]):
            if img[i][j] == 0:
                await loop.run_in_executor(executor, nx.press_buttons, controller_index, [nxbt.Buttons.A])
            await loop.run_in_executor(executor, nx.press_buttons, controller_index, [nxbt.Buttons.DPAD_RIGHT])

            if user_input.done():
                with open('.splatoon-painter.archieve', 'w') as f:
                    f.write('%d %d' % (i, j))
                break

        start[1] = 0
        await loop.run_in_executor(executor, nx.tilt_stick, controller_index,
                                   nxbt.Sticks.LEFT_STICK, -100, 0, 7.5)
        await loop.run_in_executor(executor, nx.press_buttons, controller_index, [nxbt.Buttons.DPAD_DOWN])

        if user_input.done():
            break

    # Save and remove the controller
    await loop.run_in_executor(executor, nx.press_buttons, controller_index, [nxbt.Buttons.MINUS])
    await loop.run_in_executor(executor, nx.remove_controller, controller_index)


def main():
    # Check su permission
    if not os.geteuid() == 0:
        raise PermissionError('Script must be run as root!')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename', help='The file address of the .bmp file to be input')
    parser.add_argument('-r', '--reconnect', action='store_true',
                        help='If the switch has already been paired.')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args, loop))
    loop.close()

    
if __name__ == "__main__":
    main()
