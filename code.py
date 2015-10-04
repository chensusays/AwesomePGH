import logging
import webapp2

#from google.appengine.ext.webapp import template
from google.appengine.api import users


#retrieve and render template
#def render_template(handler, templatename, templatevalues):
# path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
# html = template.render(path, templatevalues)
# handler.response.out.write(html)

class MainPageHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
        (user.nickname(), users.create_logout_url('/')))
    else:
      greeting = ('<a href="%s">Sign in or register</a>.' % 
        users.create_login_url('/'))

    self.response.out.write("<html><body>%s</body></html>" % greeting)

url_list = [
  ('/', MainPageHandler)
]

app = webapp2.WSGIApplication(url_list)