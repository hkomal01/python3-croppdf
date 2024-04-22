# python3-croppdf
Crops the bottom of PDFs to remove watermarks

## Requirements
You'll need the following Python3 library:
- pikepdf

## How to use
Run:
```console
python3 croppdf.py {int : height} {file : output} {file(s): input(s)}
```
Where:
1. height
     - The number of pixels to crop from the bottom of the file
2. output
     - Where to output the file and under what name
3. input(s)
     - One or more pdf files to give as input
     - They will all be cropped using height and then concatenated in the same order they were given
