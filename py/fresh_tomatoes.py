import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script async src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        (function () {
            "use strict";

            // Pause the video when the modal is closed
            $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
                // Remove the src so the player itself gets removed, as this is the only
                // reliable way to ensure the video stops playing in IE
                $("#trailer-video-container").empty();
            });
            // Start playing the video whenever the trailer modal is opened
            $(document).on('click', '.movie-tile > img', function (event) {
                var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
                var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                  'id': 'trailer-video',
                  'type': 'text-html',
                  'src': sourceUrl,
                  'frameborder': 0
                }));
            });

            // Animate in the movies when the page loads
            $(document).ready(function () {
                $('.movie-tile').hide().fadeIn();
            });
        }());
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers - Python</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        <h2>Favorite Movies</h2>
            {movie_tiles}
        <h2>Favorite Series</h2>
            {serie_tiles}
    </div>

  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <a class="btn btn-info glyphicon glyphicon-plus" aria-hidden="true" href="#collapseSample{movie_index}" data-toggle="collapse"></a>
    <div class="collapse" id="collapseSample{movie_index}">
        {movie_storyline}
    </div>
</div>
'''


serie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img src="{poster_image_url}" width="220" height="342" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <h2>{serie_title}</h2>
    <a class="btn btn-info glyphicon glyphicon-plus" aria-hidden="true" href="#collapseSample{serie_index}" data-toggle="collapse"></a>
       <div class="collapse" id="collapseSample{serie_index}">
        {serie_storyline}
    </div>
</div>
'''


def extract_youtube_id(youtube_url):
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', youtube_url)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', youtube_url)
    trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                          else None)

    return trailer_youtube_id
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    index = 0
    for movie in movies:
        # Extract the youtube ID from the url



        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_index = "movie" + str(index),
            movie_title = movie.title,
            movie_storyline = movie.storyline,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = extract_youtube_id(movie.trailer_youtube_url)
        )
        index += 1;
    return content


def create_series_tiles_content(series):
    content = ''
    index = 0
    for serie in series:
        content += serie_tile_content.format(
            serie_index = "serie" + str(index),
            poster_image_url = serie.poster_image_url,
            serie_title = serie.title,
            serie_storyline = serie.storyline,
            trailer_youtube_id = extract_youtube_id(serie.trailer_youtube_url)
        )
        index += 1;

    return content

def open_movies_page(movies, series):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        serie_tiles = create_series_tiles_content(series))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)