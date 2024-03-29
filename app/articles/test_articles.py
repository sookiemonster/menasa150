import os, json

NUM_EVENT_PER_SECTION = 4
SECTION_NUM = 3
FILLER_BODY = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque nec interdum mi. Pellentesque suscipit fermentum vestibulum. Integer ornare suscipit ipsum, eget porta turpis sagittis id. Vivamus malesuada vel augue sed ornare. Nam accumsan tortor a sapien tincidunt, a iaculis velit semper. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam sed dolor id ipsum volutpat condimentum. Pellentesque egestas ut dui lacinia euismod. Proin interdum risus vitae felis interdum ornare. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean quis nibh odio. Quisque euismod dui libero, a efficitur augue eleifend eget. Suspendisse porta sem a finibus auctor. Curabitur id porta enim. Nulla at orci vitae mauris posuere volutpat sit amet id nulla. Maecenas suscipit eu augue efficitur tempus. Vivamus elementum mauris eu lobortis condimentum. Ut luctus ex ut mauris aliquam mattis. Quisque a elementum quam. Nulla scelerisque mi rhoncus, convallis ligula sit amet, volutpat mauris. Donec convallis euismod urna, a suscipit nisl varius quis. Etiam consequat est sed erat gravida viverra. Proin a vestibulum sapien. Sed ac tellus eu turpis malesuada dapibus eu sed lorem. Mauris aliquet egestas rutrum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi pellentesque urna ac sem molestie, nec scelerisque arcu lacinia. Pellentesque consequat commodo efficitur. Duis convallis ultricies enim, in sollicitudin turpis iaculis quis. In varius aliquam nibh ut porttitor. Morbi consectetur sapien quam, sed imperdiet purus iaculis ac. Nullam facilisis ipsum vel pharetra tempus. In mi nibh, tempor quis felis eu, malesuada congue tortor. Etiam dui quam, convallis venenatis sodales at, varius non nunc. Praesent consequat lobortis quam id imperdiet. Nunc a erat eu dui ornare pulvinar id a enim. Duis tempor felis vitae nisi euismod, a ullamcorper odio placerat. Mauris viverra augue sed diam viverra lobortis. In lectus lacus, sagittis sit amet varius vel, cursus eu orci. Nam porttitor massa tortor, id ultrices orci lobortis in. Morbi tincidunt turpis quis viverra porttitor. In maximus enim vulputate ultrices maximus. Proin imperdiet lectus eget pulvinar varius. Vivamus pulvinar libero purus, ut finibus diam porttitor eget. Nulla sed convallis quam, non aliquam nisl. Ut at maximus odio. Cras tincidunt lectus non justo sodales accumsan. Pellentesque sed efficitur ligula. Proin sagittis sem sit amet tortor fringilla mollis. Suspendisse potenti. Morbi quis congue tellus. Fusce fermentum varius orci non elementum. Cras faucibus quam sit amet mauris mollis hendrerit. Morbi quis facilisis nibh. Donec in ante sit amet purus scelerisque condimentum in quis dolor. Donec sodales consectetur urna et varius. Fusce sollicitudin nunc odio, vel ornare arcu consectetur et. Integer semper ipsum vel nunc consectetur, a condimentum felis bibendum. Vivamus consectetur justo risus, a interdum nibh ultrices vitae. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit erat, egestas eu dapibus vitae, lacinia ac eros. Morbi sit amet magna vitae mauris venenatis viverra ut ut enim."

TIMELINE_FILE = 'timeline.json'
OUTPUT = 'debug.json'

def make_article_data(section_num: int, event_num: int) -> dict: 
   global article_id
   result = {}
   result['title'] = f'{section_num}_{event_num}'
   result['timeline_title'] = f'Event {event_num}'
   result['anchor'] = str(article_id)
   result['content_file'] = f'{article_id}.txt'
   with open(f'{article_id}.txt', "w") as f:
      f.write(FILLER_BODY)
   article_id+=1

   return result


def generate_articles():
   result = {}
   global article_id
   article_id = 0
   with open(TIMELINE_FILE, "r") as f:
      result = json.loads(f.read())

   for i in range(SECTION_NUM):      
      result[f'section{i+1}']['event_list'] = []
      for j in range(NUM_EVENT_PER_SECTION):
         result[f'section{i+1}']['event_list'].append(make_article_data(i, j));

   with open(OUTPUT, "w") as f:
      json.dump(result, f)

generate_articles()