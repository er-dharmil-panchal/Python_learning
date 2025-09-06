import json
import os

import Util as ut
from Post import Post


class Social_Network:
    @staticmethod
    def get_feed(current_user):
        posts = [Post.from_dict(p) for p in ut.load_posts()]
        followers_list = ut.load_followers().get(current_user, [])

        followed_posts = [p for p in posts if p.username in followers_list or p.username == current_user]
        other_posts = [p for p in posts if p.username not in followers_list and p.username != current_user]

        final_feed = followed_posts + other_posts
        return sorted(final_feed, key=lambda x: x.created_at, reverse=True)

    @classmethod
    def update_followers(cls, current_user, target=None, action=None):
        followers = ut.load_followers()

        if target is None:
            if current_user.username not in followers:
                followers[current_user.username] = []
        else:
            if target and target.username != current_user.username:
                if action == "Follow":
                    if target.username.strip() not in followers[current_user.username]:
                        followers[current_user.username].append(target.username.strip())
                    else:
                        print("✔ Already following this user.")
                elif action == "Unfollow":
                    if target.username.strip() in followers[current_user.username]:
                        followers[current_user.username].remove(target.username.strip())
                    else:
                        print("You are not following this user.")
                else:
                    print("✖ You are not following this user.")
            else:
                print("You can't follow Yourself.")
                return

        with open("Data/followers.json", "w") as file:
            json.dump(followers, file, indent=4)

    @classmethod
    def is_following(cls, current_user, target):
        followers = ut.load_followers()
        return current_user.username in followers and target.username in followers[current_user.username]
