from starlette.requests import Request
from starlette.responses import StreamingResponse
import numpy as np
from PIL.Image import fromarray as image_from_array
from io import BytesIO

def image_byte_stream() -> BytesIO:
    image_data = np.zeros((512, 512, 3), dtype=np.uint8)

    # randomize color
    color = np.random.randint(0, 255, 3, dtype=np.uint8)
    image_data[:] = color

    image_bytes = image_from_array(image_data)

    buffer = BytesIO()
    image_bytes.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer

async def generate_image_endpoint(_: Request) -> StreamingResponse:
    return StreamingResponse(image_byte_stream(), media_type="image/png")
