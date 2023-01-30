import asyncio
 
import websockets
 
# create handler for each connection
 
async def handler(websocket, path):
 
    data = await websocket.recv()
 
    reply = f"Data recieved as:  {data}!"
 
    await websocket.send(reply)
 
 
 
start_server = websockets.serve(handler, "localhost", 8000)
 
 
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()

# https://www.piesocket.com/blog/python-websocket
# https://codepen.io/fariati/pen/mdRpEYP
# https://blog.cisne.dev/animando-um-personagem-com-css-e-javascript/
# https://www.youtube.com/watch?v=qlLzs3kTa4I