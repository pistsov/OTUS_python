from models import User, Post, db


def create_user(
    username: str,
    name: str,
    email: str
) -> User:
    user = User(name=name, username=username, email=email)

    db.session.add(user)
    db.session.commit()


def get_users() -> list[User]:
    users = User.query.order_by(User.id).paginate(per_page=10)
    return users


def get_user_by_id_or_raise(user_id: int) -> User:
    user: User = db.get_or_404(
        User,
        user_id,
        description=f"User #{user_id} not found!")
    return user


def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()


def create_post(post_title: str, post_body: str, user_id: User) -> Post:
    post = Post(
        title=post_title,
        body=post_body,
        user_id=user_id,
    )

    db.session.add(post)
    db.session.commit()


def get_posts() -> list[Post]:
    posts = Post.query.order_by(Post.id).paginate(per_page=10)
    return posts


def get_post_by_id_or_raise(post_id: int) -> Post:
    post: Post = db.get_or_404(
        Post,
        post_id,
        description=f"Post #{post_id} not found!")
    return post


def delete_post(post: Post) -> None:
    db.session.delete(post)
    db.session.commit()


def populate_users(users_data: dict) -> None:
    for user in users_data:
        create_user(
            username=user.get("username"),
            name=user.get("name"),
            email=user.get("email")
        )


def populate_posts(posts_data: dict) -> None:
    for post in posts_data:
        create_post(
            post_title=post.get("title"),
            post_body=post.get("body"),
            user_id=post.get("userId")
        )