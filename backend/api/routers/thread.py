from fastapi import APIRouter,Header,Response
from .schema import (
    Thread,
    GetResponse,
    CreateRequest,
    CreateResponse,
)

import crud

router = APIRouter()

@router.get("/threads", response_model=GetResponse, status_code=200)
async def get():
    threads_date = crud.get()
    threads_list = []
    for thread_date in threads_date:
        thread = Thread(
            id=thread_date[0],
            user_name=thread_date[1],
            content=thread_date[2]
        )
        
        threads_list.append(thread)
    return GetResponse(result=threads_list)


@router.post("/threads", response_model=CreateResponse, status_code=201)
async def post(request:CreateRequest):
    dummy_id = 999
    response = CreateResponse(
        id=dummy_id,
        user_name=request.user_name,
        content=request.content
    )
    return response


@router.put("/threads/{thread_id}",response_model=GetResponse,status_code=200)#値の更新
async def update(thread_id: int):
    response = [
    Thread(
        id=thread_id,
        user_name="aaa",
        content="aaa",
    ),
    ]
    return  GetResponse(results=response)


@router.delete("/threads/{thread_id}", status_code=204)
async def delete(thread_id: int):
    response= DeleteResponse(
        user_name="",
        content= "")

