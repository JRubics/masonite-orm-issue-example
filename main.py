from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class User(Model):
    __table__ = "users"

class Website(Model):
    __table__ = "websites"

    @belongs_to('user_id', 'id')
    def user(self):
        return User

user_name = 'user1'
user = User.create({'name': user_name})
website = Website.create({'user_id': user.id})

query = Website.where_has(
            'user',
            lambda q: q.where('name', '=', user_name)
        )

print("Query before count:")
print(query.to_sql())

count_query = query.new_from_builder()
count = count_query.count()

print("\nQuery after count:")
print(query.to_sql())