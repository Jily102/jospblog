from rest_framework import serializers

from core.models import Post

class PostSerializer(serializers.ModelSerializer):
    post_views = serializers.SerializerMethodField()
    api_url = serializers.HyperlinkedIdentityField(view_name='api-post-detail', lookup_field='pk')
    post_url = serializers.HyperlinkedIdentityField(view_name='post-detail', lookup_field='slug')


    def get_post_views(self, obj):
        try:
            return obj.hit_count.hits
        except:
            pass

    class Meta:
        model = Post
        fields = ('api_url', 'post_url', 'title', 'descript', 'post_views')