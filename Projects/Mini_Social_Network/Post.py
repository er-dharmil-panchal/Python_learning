import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import Util as ut

post_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "content": {"type": "string"},
        "username": {"type": "string"},
        "created_at": {"type": "string"},
    },
    "required": ['content', 'username', 'created_at']
}


class Post:
    def __init__(self, title, content, username, created_at):
        self.title = title
        self.content = content
        self.username = username
        self.created_at = created_at
        self.valid = False

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_username(self):
        return self.username

    def get_created_at(self):
        return self.created_at

    @classmethod
    def from_dict(cls, data):
        """Build Post object from dict loaded from JSON"""
        return cls(
            title=data['title'],
            content=data['content'],
            username=data['username'],
            created_at=data['created_at']
        )

    def create_post(self):
        posts = ut.load_posts()
        new_post = {
            "title": self.get_title(),
            "content": self.get_content(),
            "username": self.get_username(),
            "created_at": self.get_created_at(),
        }
        try:
            validate(instance=new_post, schema=post_schema)
            self.valid = True
        except ValidationError as e:
            print(f"❌ Invalid Format: {e.message}")

        if self.valid:
            posts.append(new_post)
            with open("Data/posts.json", "w") as file:
                json.dump(posts, file, indent=4, ensure_ascii=False)
        else:
            print("There is some problem in formating, please try again.")

    @classmethod
    def get_post_by_username(cls, username):
        posts = [Post.from_dict(post) for post in ut.load_posts()]
        needed_post = [post for post in posts if post.username == username]
        return needed_post

