from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import aiosqlite


DATABASE_URL = "test.db"


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def some_startup_task():
    print('startup')

    db = await aiosqlite.connect(DATABASE_URL)
    await db.execute("create table IF NOT EXISTS user (username, password);")


async def some_shutdown_task():
    print('shutdown')


routes = [Route('/', homepage)]

app = Starlette(debug=True,
    routes=routes,
    on_startup=[some_startup_task],
    on_shutdown=[some_shutdown_task])


# READ
# SELECT ONE

# SELECT ALL

# CREATE
# INSERT

# UPDATE

# DELETE


