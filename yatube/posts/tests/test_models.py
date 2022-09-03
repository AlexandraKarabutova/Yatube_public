from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post, Comment, Follow

User = get_user_model()
POST_LIMIT: int = 15


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = User.objects.create_user(username='auth')
        cls.user = User.objects.create_user(username='user')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=PostModelTest.author,
            text='Тестовый длинный пост',
        )
        cls.comment = Comment.objects.create(
            post=PostModelTest.post,
            author=PostModelTest.user,
            text='Текст комментария'
        )
        cls.follow = Follow.objects.create(
            user=PostModelTest.user,
            author=PostModelTest.author
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        group = PostModelTest.group
        expected_group_name = group.title
        post = PostModelTest.post
        expected_post_name = post.text[:POST_LIMIT]
        comment = PostModelTest.comment
        expected_comment_name = f"Комментарий: '{comment.post}', Автор: {comment.author}"
        follow = PostModelTest.follow
        expected_follow_name = f"Подписка {follow.user} на {follow.author}"
        object_names = {
            expected_group_name: str(group),
            expected_post_name: str(post),
            expected_comment_name: str(comment),
            expected_follow_name: str(follow),
        }
        for value, expected in object_names.items():
            with self.subTest(value=value):
                self.assertEqual(value, expected)
