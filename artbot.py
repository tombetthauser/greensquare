from datetime import date

class ArtBot:
  def __init__(self):
    self.creation_date = date.today()

  """ General Notes...

    ArtBot Input / Output Examples:

    floor_matrix = [
      -----------------
      |            XXX|
      |            XXX|
      \              |
        \       -------
      |         |
      |         |
      -----------
    ]

    floor_matrix = [
      [1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 3, 1],
      [1, 0, 0, 0, 3, 1],
      [2, 0, 0, 0, 0, 1],
      [2, 0, 0, 1, 1, 1],
      [2, 0, 0, 1, 3, 3],
      [1, 0, 0, 1, 3, 3],
      [1, 1, 1, 1, 3, 3],
    ]

    0 => 1 square foot of gallery floor space
    1 => 1 foot of gallery wall
    2 => 1 floor of gallery door or window
    3 => 1 square foot of unusable space (desk, outside etc)



    arguments:
      artworks –- an list of artwork_objects
      walls -- an list of nested tuples with height and width 
      floor -- optional matrix representing floorplan for sculpture layout
      
      artwork_object -- objects for artworks
        ie {
          title: "Mona Lisa"
          type: [painting, drawing, sculpture, video etc]
          height: 22 [inches]
          width: 12 [inches]
          etc...
        }
  """

  def select_artists(self, artists_array):
    # return array
    pass

  def hang_show(self, artworks, walls, floor):
    # return array
    # return array
    pass


# -------------------------------------


new_bot = ArtBot()
new_bot.test()
