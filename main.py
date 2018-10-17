import webapp2
import jinja2
import os
import json


#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/images.html')
        self.response.write(template.render())

class Portraits(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/portraits.html')
        self.response.write(template.render())

class Places(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/places.html')
        self.response.write(template.render())

class Contact(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/contact.html')
        self.response.write(template.render())

class Jenessa(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/ness.html')
        self.response.write(template.render())

class Tessa(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/tess.html')
        self.response.write(template.render())

class Elisha(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/elisha.html')
        self.response.write(template.render())

class Alycia(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/lyc.html')
        self.response.write(template.render())

class Valeria(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/val.html')
        self.response.write(template.render())

class Stian(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/stian.html')
        self.response.write(template.render())

class Bloedel(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/bloedel.html')
        self.response.write(template.render())

class Canada(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/canada.html')
        self.response.write(template.render())

class GlowChristmas(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/glow.html')
        self.response.write(template.render())

class Seattle(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/seattle.html')
        self.response.write(template.render())

class Sky(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/sky.html')
        self.response.write(template.render())

class LittleSi(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/littlesi.html')
        self.response.write(template.render())

class OlympicNationalPark(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/hike.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/images', ImageHandler),
    ('/portraits', Portraits),
    ('/places', Places),
    ('/contact', Contact),
    ('/jenessa', Jenessa),
    ('/tessa', Tessa),
    ('/elisha', Elisha),
    ('/alycia', Alycia),
    ('/valeria', Valeria),
    ('/stian', Stian),
    ('/bloedelconservatory', Bloedel),
    ('/canada', Canada),
    ('/glowchristmas', GlowChristmas),
    ('/seattle', Seattle),
    ('/sky', Sky),
    ('/littlesi', LittleSi),
    ('/olympicnationalpark', OlympicNationalPark)
], debug=True)
