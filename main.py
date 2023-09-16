# import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse, JSONResponse

# from kv import KV

app = FastAPI()
# kv = KV()


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


# class Post(BaseModel):
#     title: str = Field(title="The title of post")
#     content: str = Field(title="The content of post")
#     writer: str = Field(title="The writer of post")


# @app.get("/health")
# async def health_check():
#     return "OK"


# @app.get("/public/{file_path}")
# async def static_file_response(file_path: str):
#     dir_name = os.path.dirname(__file__)
#     return FileResponse(os.path.join(dir_name, "public", file_path))


# @app.post("/posts/{post_id}")
# async def write_post(post: Post, post_id: str):
#     print(post)

#     result = kv.set(f"post:{post_id}", dict(post))
#     return JSONResponse(result)


# @app.get("/posts/{post_id}", response_model=Post)
# async def get_post(post_id: str):
#     result = kv.get(f"post:{post_id}")

#     if not result:
#         raise HTTPException(status_code=404)

#     return JSONResponse(eval(result))


# @app.get("/{current_path}")
# def path(current_path):
#     return {"path": current_path}
