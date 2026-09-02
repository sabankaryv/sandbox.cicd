# 1.latent bridge
# status codes
# contentxt managers
# pickling
# pydantic 
# diff between fastapi and django
# how to use global exception
# how to save the images into aws bucket
# program
#1. def test(x=[]): 
#     x.append(1) 
#     return x 
    
# print(test()) #==>[1]
# print(test()) #==>[1,1]
# 2.
# requests = [
#     {"user_id": 101, "endpoint": "/orders"},
#     {"user_id": 102, "endpoint": "/users"},
#     {"user_id": 101, "endpoint": "/orders"},
#     {"user_id": 103, "endpoint": "/orders"},
#     {"user_id": 102, "endpoint": "/users"},
#     {"user_id": 101, "endpoint": "/payments"},
# ]


# def checkendpointcount(requests):
#     seen = {}

#     for request in requests:
#         key = (request["user_id"], request["endpoint"])

#         if key in seen:
#             seen[key] += 1
#         else:
#             seen[key] = 1

#     print(seen)


# checkendpointcount(requests)
