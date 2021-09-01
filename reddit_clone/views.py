from django.core.checks.messages import Error
from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from .models import Subreddit, Vote
from .serializers import SubredditSerializer, VoteSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from reddit_clone import serializers

# Create your views here.

class SubredditList(generics.ListCreateAPIView):
    queryset = Subreddit.objects.all()
    serializer_class = SubredditSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serialzer):
        serialzer.save(poster = self.request.user)

class SubredditDetailView(APIView):
    def get(self, request, pk):
        queryset=Subreddit.objects.get(id=pk)
        serializer = SubredditSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class VoteCreate(generics.CreateAPIView):
#     serializer_class = VoteSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         subreddit = Subreddit.objects.get(pk=self.kwargs['pk'])
#         # subreddit = Subreddit.objects.get(id=pk)
#         serializer = VoteSerializer(subreddit, read_only=True)
#         print(serializer)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def perform_create(self, serialzer):
#         serialzer.save(voter=self.request.user, subreddit=Subreddit.objects.get(pk=self.kwargs['pk']))

class VoteCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        user = self.request.user
        subreddit = Subreddit.objects.get(id=pk)
        # serializer = VoteSerializer(data=request.data)
        serializer = VoteSerializer(subreddit, read_only=True)
        dual = Vote.objects.filter(voter=user, post=subreddit)
        print (dual)
        if dual.exists():
            raise ValidationError('The vote already exists!!')
        else:
            vote = Vote.objects.create(voter=user, post=subreddit)
        return Response(serializer.data)

class VoteAPIListView(APIView):
    def get(self, request):
        queryset = Vote.objects.all()
        # print(queryset)
        serializer = VoteSerializer(queryset, many=True)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VoteAPIDetailListView(APIView):
    def get(self, request, pk):
        queryset = Vote.objects.get(id=pk)
        # print(queryset)
        serializer = VoteSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

class VoteAPIDeleteView(APIView):
    def delete(self, request, pk):
        queryset = Vote.objects.get(id=pk)
        serializer = VoteSerializer(queryset, many=False)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)