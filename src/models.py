from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    posts=relationship("Post", back_populates="user")
    comment=relationship("Comment", back_populates="user")

    folowers= relationship("Follower", back_populates="user_from")
    folowing= relationship("Follower", back_populates="user_to")

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    user=relationship("User", back_populates="posts")
    comments=relationship("Comment", back_populates="post")
    media=relationship("Media", back_populates="post")

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(1000), nullable=False)

    author_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    user=relationship("User", back_populates="comment")

    post_id: Mapped[int]= mapped_column(ForeignKey("post.id"))
    post=relationship("Post", back_populates="comments")

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    url: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    post_id: Mapped[int]= mapped_column(ForeignKey("post.id"))
    post=relationship("Post", back_populates="media")

class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    user_from=relationship("User", foreign_keys=[user_from_id])
    user_to_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    user_to=relationship("User", foreign_keys=[user_to_id])

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


#     def serialize(self):
#         return {"
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
