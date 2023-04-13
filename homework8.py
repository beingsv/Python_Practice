#1 What is meant by stateless nature in RestAPI?

#In REST API, the stateless nature means that the server does not store any client context between requests.


#2 403, 503, 301 Status Codes?

#403 Forbidden: The 403 status code means that the server understands the request, but it refuses to fulfill it.
#503 Service Unavailable: The 503 status code indicates that the server is currently unable to handle the request due to maintenance or overload.
#301 Moved Permanently: The 301 status code means that the requested resource has been permanently moved to a new URL. 



#3 USE public API and use all http methods on it.
import requests

# Set the base URL for the API
base_url = "https://jsonplaceholder.typicode.com"

# Use the GET method to retrieve a list of resources
response = requests.get(f"{base_url}/posts")

# Print the response status code and content
print(response.status_code)
print(response.content)

# Use the POST method to create a new resource
new_post = {"title": "New Post", "body": "This is a new post."}
response = requests.post(f"{base_url}/posts", json=new_post)

# Print the response status code and content
print(response.status_code)
print(response.content)

# Use the PUT method to update a resource
updated_post = {"title": "Updated Post", "body": "This post has been updated."}
response = requests.put(f"{base_url}/posts/1", json=updated_post)

# Print the response status code and content
print(response.status_code)
print(response.content)

# Use the PATCH method to partially update a resource
patched_post = {"title": "Patched Post"}
response = requests.patch(f"{base_url}/posts/1", json=patched_post)

# Print the response status code and content
print(response.status_code)
print(response.content)

# Use the DELETE method to delete a resource
response = requests.delete(f"{base_url}/posts/1")

# Print the response status code and content
print(response.status_code)
print(response.content)
