from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_password)

# Now that we have Alembic, se don't actually need the next command.
# This is the command that tolds sqlalchemy to run the creat statement so 
# that it generates all of the tables when it first start it up. 
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
    

@app.get("/")
def root():
    return {"message": "Hello World!"}



#------------------------------------------------------------------
# CRUD operations using Postman and with NO actual database

# from random import randrange

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorite food", "content": "I like pizza", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     print(post.title)
#     print(post.published)
#     print(post.rating)
#     #print(post)
#     #print(post.dict())
#     post_dict = post.dict()
#     post_dict['id'] = randrange(0, 1000000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts) - 1]
#     return {"detail": post}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return {"post_detail": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     post_dict = post.dict()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
#     return {"data": post_dict}



# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}

#------------------------------------------------------------------

# @app.get("/")
# async def root():
#     return {"message": my_posts}

# @app.post("/createposts")
# def create_posts(payLoad: dict = Body()):
#     print(payLoad)
#     return {"new_post": f"title: {payLoad['title']}; content: {payLoad['content']}"}
