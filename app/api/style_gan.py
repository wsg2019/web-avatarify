import base64
import json
import os
import time
import typing
import uuid
from pathlib import Path
import base64
import cv2
import numpy as np
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import BaseModel
import requests
from app import io, security, types

router = APIRouter()


class Response(BaseModel):
    avatar: types.Image


@router.get("")
def get_avatar(credentials: HTTPAuthorizationCredentials = security.http_credentials,):
    url = "https://thispersondoesnotexist.com/image"
    r = requests.get(url, headers={"User-Agent": "My User Agent 1.0"}).content

    image = io.bytes2image(r)
    image = cv2.resize(image, (512, 512))
    r = io.image2bytes(image)
    # print(image.shape)

    base64image = base64.b64encode(r)
    return Response(avatar=types.Image(content=base64image))
