from urllib.request import urlopen, quote
import json
import shutil
import os

# Add other values according to your requirement
values = ['.', '[', ']', '(', ')', 'm720p', '480p', '480', '1080p', '720p', 'DVDSCR', 'BrRip', 'BRRIp', 'New Source', 'MP3',
          'mkv', 'mSD', '2CD', 'BRRip', 'BRrip','BDRip', '720p', 'Blu','Ray', 'mp4', 'XviD', '-', 'x264', 'ETRG', 'avi'
         , 'DVD', 'dvd', 'DVDRip', 'RIP', 'rip', 'Rip', 'HDRip' , "Director's Cut",
          'Dual', 'Audio', 'Eng', 'Hindi', 'KORSUB', 'Blu-RayRip', 'PRE']


def find(unsortedMoviesFolder, sortedMoviesFolder):
    for movie in os.listdir(unsortedMoviesFolder):
        year = None
        movieName = movie
        for y in range(1500, 2100):
            if (str(y) in movie):
                year = str(y)
                movie = movie.replace(str(y), " ")
        for z in values:
            if (str(z) in movie):
                movie = movie.replace(str(z), " ")
            if ("  " in movie):
                movie = movie.replace("  ", " ")
        if (year == None):
            url = 'http://www.omdbapi.com/?t=' + quote(str(movie))
        else:
            url = 'http://www.omdbapi.com/?t=' + quote(str(movie)) + '&y=' + year
        response = urlopen(url).read()
        response = response.decode('utf-8')
        jsonvalues = json.loads(response)
        if jsonvalues["Response"] == "True":
            imdbrating = jsonvalues['imdbRating']
            destinationDirLocation = sortedMoviesFolder + '\\' + imdbrating + '_' + movieName
            srcFileLocation = unsortedMoviesFolder + '\\' + movieName
            if not os.path.exists(destinationDirLocation):
                os.makedirs(destinationDirLocation)
            shutil.move(srcFileLocation, destinationDirLocation)


#Change the location of the folder accordingly
find('C:\\video\\Bollywood', 'C:\\video\\BollywoodImdb')