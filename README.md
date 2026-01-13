# check_dupes_and_transfer

A suite of media file utilities for organization and space saving.

## find_dupes

Finds duplicate media files in a designated directory by comparing their contents using hashes.
The output is a Text file listing media paths of duplicate media files.

## prune_media

Uses the same method as find_dupes to locate duplicate media files, and then moves all but one
copy to the trash.

## organize

Analyzes specified directory content's media files and organizes them. The files are placed in
folders by their creation year and renamed to <Timestamp>_<device>, i.e. "12-26-2019_23:59:59_iPhone.heic". Unsupported files types or files that have EXIF which cannot be read will be placed in a MISC folder.

## Dependencies
In addition to the python packages in requirements.txt, EXIFtool command line program also needs to be installed. It can be found here https://exiftool.org

images
'EXIF:Make': 'Apple',
'EXIF:Model': 'iPhone 8',

Video (MP4)
'QuickTime:AndroidMake': 'Google',
 QuickTime:AndroidModel': 'Pixel 7 Pro',
