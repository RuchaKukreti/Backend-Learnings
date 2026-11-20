#todo {"index":0,"title":"dance","duration":20,"status":0}
#db
to_do=[{"index":0, "title":"dance","duration":20,"status":0},
       {"index":1,"title":"singing","duration":20,"status":0},
       {"index":2,"title":"study","duration":20,"status":0},
       {"index":3,"title":"work","duration":0,"status":0}
       ]

from fastapi import FastAPI

rucha =FastAPI()

@rucha.get("/todo/{index}")
async def get_todo(index : int):
    for to_do_item in to_do:
        if to_do_item["index"] ==index:
            return to_do_item
    return {"error": "Todo not found"}

@rucha.post("/todo")
async def create_to_do():
    index=len(to_do)
    to_do.append({"index":index, "title":"reading","duration":20,"status":0})
    return to_do[index]

@rucha.put("/todo/{index}")
async def update_to_do(index: int, title: str, duration :int, status: bool):
    for to_do_item in to_do:
        if(to_do_item["index"]==index):
            to_do_item["title"] =title
            to_do_item["duration"]=duration
            to_do_item["status"]=status
            return to_do_item
    return {"error": "Todo not found"}

@rucha.patch("/todo/{index}")
async def patch_to_do(index :int, title: str | None = None, duration :int | None = None, status:bool | None = None):
    for to_do_item in to_do:
        if to_do_item["index"] ==index:
            if title is not None:
                to_do_item["title"]=title
            if duration is not None:
                to_do_item["duration"]=duration
            if status is not None:
                to_do_item["status"]=status
            return to_do_item
    return {"error":"Todo not found"}

@rucha.delete("/todo/{index}")
async def delete_to_do(index: int):
    for to_do_item in to_do:
        if to_do_item["index"]==index:
            to_do.remove(to_do_item)
            return {"message": "Todo deleted"}
    return {"error":"Todo not found"}


    