from starlette.requests import Request
from starlette.responses import StreamingResponse
import numpy as np
from PIL.Image import fromarray as image_from_array
from io import BytesIO

def image_byte_stream() -> BytesIO:
    zeroes = np.zeros((512, 512, 3), dtype=np.uint8)
    image_bytes = image_from_array(zeroes)

    buffer = BytesIO()
    image_bytes.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer

async def generate_image_endpoint(_: Request) -> StreamingResponse:
    return StreamingResponse(image_byte_stream(), media_type="image/png")
