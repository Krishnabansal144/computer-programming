#q3
# The output should be user-friendly, but the code part is also important.
#  Well-structured and readable code is very important
#  for being a good programmer. Now it's up to you to decide, which formatting method to choose.
# 
# Imagine you need to compose a dynamic URL for every certain user with user-specific details. Suppose,
#  you want to send different URLs for 
# every user, depending on their name and profession. The base would be something like
# 
# "http://example.com/nickname/desirable/profession/profile", where nickname and profession are 
# prompts from a user and are dynamic.
# 
# Read the nickname and profession of the user from the input and print a user-specific URL. 
# Don't bother about any rules of composing the URLs and just use raw input to accomplish the task.

nick_name = input()
profession = input()
print(f'http://example.com/{nick_name}/desirable/{profession}/profile')
