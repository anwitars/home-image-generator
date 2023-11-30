import uvicorn
import click

from home_image_generator.starlette.app import app

@click.command()
@click.option('--port', default=8000, help='Port to run the server on.')
@click.option('--host', default='127.0.0.1', help='Host to run the server on.')
def main(port: int, host: str):
    uvicorn.run(app, host=host, port=port)

if __name__ == '__main__':
    main()
