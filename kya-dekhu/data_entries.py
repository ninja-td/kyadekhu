class MovieEntry(db.model)
  title = db.StringProperty(required=true)
  display_name = db.StringProperty()
  alternate_names = db.StringProperty()
  trailer_link = db.StringProperty()
  songs = db.ListProperty()
  review = db.StringProperty()
  rating = db.IntegerProperty()
  mood = db.ListProperty()
  
  
class MovieListEntry(db.model)
  name = db.StringProperty(required = true)
  display_name = db.StringProperty()
  movies = db.ListProperty()
  
