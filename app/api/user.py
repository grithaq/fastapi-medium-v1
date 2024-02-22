import repositories
from fastapi import APIRouter, status
from schema import UserSchema, ListUserSchema


router = APIRouter()


@router.get(
        '/user', tags=['Users'],
        status_code=status.HTTP_200_OK,
        response_model=ListUserSchema
)
def get_all_users():
    users = repositories.db_users.get()
    lus = ListUserSchema(message="Success", status=str(status.HTTP_200_OK), data=users)
    return lus
    

@router.post('/user', tags=['Users'])
def create_user(user: UserSchema):
    users = repositories.db_users.add(user.model_dump(exclude_unset=True))
    lus = ListUserSchema(message="Success", status=str(status.HTTP_201_CREATED), data=users)
    return lus


@router.put(
    "/user/{id}", tags=['Users'],
    response_model=ListUserSchema,
    status_code=status.HTTP_200_OK
)
def update_user(id: str, user: UserSchema):
    users = repositories.db_users.update_user(
        id, user.model_dump(exclude_unset=True))
    data = {
        "message": "Success",
        "status": str(status.HTTP_200_OK),
        "users": users
    }
    return data
