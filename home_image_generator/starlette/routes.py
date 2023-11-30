from starlette.routing import Route

from home_image_generator.endpoints.generate_image import generate_image_endpoint

routes = [Route("/", generate_image_endpoint, methods=["GET"])]
