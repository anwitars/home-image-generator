from starlette.routing import Route

from home_image_generator.endpoints.api.generate_image import generate_image_endpoint

routes = [Route("/api/generate_image", generate_image_endpoint, methods=["GET"])]
