'''
ASSIGNMENT CHECKPOINT-1 (ITTWIST)
Mimic a simple blog commandline program:

Suppose you are planning to create your own blog application. Where you can read a post,
create a post, update a post or delete a post.

1. Create a list (posts) that will contain all post (dictionaries).
2. A post dictionary will contain following attributes, please refer to function calls:
  * a post id (post_id)
  * a post name (post_name)
  * a post author (post_author)
3. Create a following functions:
  * read_post which will print the posts list.
  * create_post which will accept a arbitrary keyword arguments, and push a dictionary
    in the posts list.
  * update_post which will accept a arbitrary keyword arguments, and update a dictionary
    of the respective post_id.
  * delete_post which will accept post_id as a argument, and delete that dictionary of the
    respective post_id.
4. The following function calls are already written for you, please call them respectively and verify the expected output.
   create_post
   create_post
   create_post
   read_post
   update_post
   read_post
   delete_post
'''


posts = []

#Create a post, Please change the parameter list accordingly
def create_post():
    pass

#Update a specific post, Please change the parameter list accordingly
def update_post():
    pass

#Read all post, Please add the print statement for updating the posts
def read_post():
    #print statement
    pass

#Delete a specific post, Please change the parameter list accordingly
def delete_post():
    pass

#This will call the create post function
create_post(post_id=1,post_name='Python Course Part-1',post_author='John')
create_post(post_id=2,post_name='Python Course Part-2',post_author='Bill')
create_post(post_id=3,post_name='Python Course Part-3',post_author='Jack')
#This will call the read post function
read_post()
'''Expected Output : 
[
{'post_id': 1, 'post_name': 'Python Course Part-1', 'post_author': 'John'}, 
{'post_id': 2, 'post_name': 'Python Course Part-2', 'post_author': 'Bill'}, 
{'post_id': 3, 'post_name': 'Python Course Part-3', 'post_author': 'Jack'}
]
'''
#This will call the update post function
update_post(post_id=1,post_name='Python Course Part-0',author='Max')
read_post()
''' Expected Output:
[
{'post_id': 1, 'post_name': 'Python Course Part-0', 'post_author': 'Max'}, 
{'post_id': 2, 'post_name': 'Python Course Part-2', 'post_author': 'Bill'}, 
{'post_id': 3, 'post_name': 'Python Course Part-3', 'post_author': 'Jack'}
]
'''
#This will call the delete post function
delete_post()
read_post()
''' Expected Output:
[
{'post_id': 1, 'post_name': 'Python Course Part-0', 'post_author': 'Max'}, 
{'post_id': 2, 'post_name': 'Python Course Part-2', 'post_author': 'Bill'}
]
'''
