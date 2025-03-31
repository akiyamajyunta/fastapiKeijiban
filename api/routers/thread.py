from fastapi import APIRouter
from .schema import (
    Thread,
    GetResponse,
    CreateRequest,
    CreateResponse,
    UpdateRequest,
    UpdateResponse
)


router = APIRouter()


@router.get("/threads/hello")
async def hello():
    return "hello! from thread"


@router.get("/threads", response_model=GetResponse, status_code=200)
async def get():
    dummy_threads = [
        Thread(id=1, user_name="aoki", content="ああああ"),
        Thread(id=2, user_name="akiyama", content="hello from threads"),
    ]
    return GetResponse(results=dummy_threads)


@router.post("/threads", response_model=CreateResponse, status_code=201)
async def post(request: CreateRequest):
    dummy_id = 999
    response = CreateResponse(
        id=dummy_id,
        user_name=request.user_name,
        content=request.content
    )
    return response


@router.put("/threads/{thread_id}", status_code=200)#値の更新
async def update(thread_id: int, request: UpdateRequest):
    response = UpdateResponse(
        id=thread_id,
        content=request.content
    )
    return response


@router.delete("/threads/{thread_id}", status_code=204)
async def delete(thread_id: int):
    return ""
