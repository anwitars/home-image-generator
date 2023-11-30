from starlette.applications import Starlette
from home_image_generator.starlette.routes import routes

app = Starlette(debug=True, routes=routes)
