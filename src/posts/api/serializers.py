from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )


from account.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish'
        ]


post_detail_url = HyperlinkedIdentityField(
        view_name='api-detail',
        lookup_field='slug'
        )


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',
            'publish',
            'image',
            'comments',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments



class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]



# class PostListSerializer(ModelSerializer):
#     url = post_detail_url
#     user = SerializerMethodField()
#     class Meta:
#         model = Post
#         fields = [
#             'url',
#             'user',
#             'title',
#             'content',
#             'publish',
#         ]

    # def get_user(self,obj): 
    # 	return str(obj.user.username)





""""
from posts.models import Post
from posts.api.serializers import PostDetailSerializer
data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",
    
}
add 
new_item = PostDetailSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

update
obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


delete
obj.delete()







"""