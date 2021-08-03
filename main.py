from aiohttp import web


async def get_handler(request):
    return web.Response(text=f'GET {request.match_info["search_request"]}')


async def delete_handler(request):
    return web.Response(text="DELETE")


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get('/{search_request}', get_handler),
        web.delete('/', delete_handler)
    ])
    web.run_app(app)
