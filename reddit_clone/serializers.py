from rest_framework import serializers
from .models import Subreddit, Vote

class SubredditSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = 'postingman')
    class Meta:
        model = Subreddit
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    # voter = VoteSerializer(read_only=True)
    post = SubredditSerializer(read_only=True)
    class Meta:
        model = Vote
        fields = ['id', 'post']