from entity import User


class UserRepository:
    users = []

    def get(self):
        return self.users
    
    def add(self, user):
        user_model = User()
        user_model.id = user["id"]
        user_model.username = user["username"]
        user_model.email = user["email"]
        user_model.name = user["password"]
        self.users.append(user)
        return user_model
    
    def update(self, id: str, user):
        for index, usr in enumerate(self.users):
            if usr['id'] == int(id):
                self.users[index] = user
                return self.get()
        return "User not found"
    
    def delete(self, id: str):
        for index, user in enumerate(self.users):
            if user['id'] == int(id):
                del self.users[index]
                return self.get()
        return "User not found"
    

db_users = UserRepository()