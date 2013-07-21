from google.appengine.api import users
import logging

AUTHENTICATION_LEVEL = {'EDITOR':['tanmay', 'a@a.com', 'tanmay.dehury']}
class NotLoggedInException(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

def has_access(level):
  user = users.get_current_user()
  if not user:
    raise NotLoggedInException("not logged in")
  if user.nickname() in AUTHENTICATION_LEVEL[level]:
    return True
  logging.info(user.nickname())
  return False
  
 
def get_login_url(return_url):
  return users.create_login_url(return_url)