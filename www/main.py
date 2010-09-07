from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from django.utils import simplejson

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')

class NextHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(simplejson.dumps({'filename': 'gruemangroup/theme.mp3'}))

def main():
    application = webapp.WSGIApplication([
        ('/', MainHandler),
        ('/next.json', NextHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
