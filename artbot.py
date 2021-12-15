from datetime import date

import random

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

  def find_new_artist(self, desired_artist_count):
    # use webscraper looking for artists
    pass

  def select_artists_for_show(self, desired_artist_count, artists_list):
    output_artists_list = []
    remaining_artists_list = artists_list.copy()

    while len(output_artists_list) < desired_artist_count:
      random_list_index = random.randint(1, len(remaining_artists_list))
      
      list_split_a = remaining_artists_list[0:random_list_index]
      list_split_b = remaining_artists_list[random_list_index:len(remaining_artists_list)]
      
      random_artist = list_split_a.pop()
      output_artists_list.append(random_artist)
      
      remaining_artists_list = list_split_b + list_split_a

    return output_artists_list


  def hang_show(self, artworks, walls_list):
    # return array
    # return array
    pass


# -------------------------------------


new_bot = ArtBot()
artists = [
  {"name": "Tom", "visual_index": 2341},
  {"name": "Jack", "visual_index": 2341},
  {"name": "Lana", "visual_index": 2341},
  {"name": "Rhine", "visual_index": 2341},
  {"name": "Ella", "visual_index": 2341},
  {"name": "Erin", "visual_index": 2211}
]
print([ele["name"] for ele in new_bot.select_artists_for_show(3, artists)])
