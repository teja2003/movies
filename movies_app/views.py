from django.shortcuts import render
from rest_framework.decorators import api_view 
from pymongo import MongoClient
from django.http import JsonResponse

client=MongoClient()
db = client['movies']

@api_view(['GET'])
def get_first_mov(request):
    collection=db['movies']
    cursor=collection.aggregate([{"$group":{"_id":"$director","count":{"$sum":1}}}, {"$sort":{"count":-1}},{"$limit":1}])
    data=list(cursor)
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def most_popular_genre(request):
    collection=db['movies']
    cursor=collection.aggregate([{"$group":{"_id":"$genre", "count":{"$max":"$99popularity"}}},{"$sort":{"count":-1}},{"$limit":1}])
    data=list(cursor)
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def top_ten_movies(request):
    collection=db['movies']
    cursor=collection.aggregate([{"$group":{"_id":"$name","maxlen":{"$max":"$imdb_score"}}},{"$limit":10}])
    data=list(cursor)
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def least_watched_movie(request):
    collection=db['movies']
    cursor=collection.aggregate([{"$group":{"_id":"$name","maxlen":{"$min":"$imdb_score"}}},{"$limit":1}])
    data=list(cursor)
y    return JsonResponse(data,safe=False)


@api_view(['GET'])
def best_director_in_top100(request):
    collection=db['movies']
    cursor=collection.aggregate([{"$group":{"_id":"$director","maxlen":{"$max":"$imdb_score"}}},{"$sort":{"count":-1}},{"$limit":1}])
    data = list(cursor)
    return JsonResponse(data,safe=False)

@api_view(['POST'])
def get_post(request):
    collection=db['movies']
    req=request.data
    cursor=collection.insert([{
	"99popularity" : req["99popularity"],
	"director" : req["director"],
	"genre" : req["genre"],
	"imdb_score" : req["imdb_score"],
	"name" : req["name"]
    }])
    return JsonResponse({"msg":"Data added successfully"},safe=False)



