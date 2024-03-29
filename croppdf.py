import pikepdf
import sys

def cropcat(inp, out, height):
    # Create output PDF page
    final = pikepdf.Pdf.new()
    # Loop through each PDF file and concatenate 
    # cropped pages onto output PDF file
    for pdf in inp:
        curr = pikepdf.open(pdf)
        for page in curr.pages:
            page.MediaBox[1] += height
            final.pages.append(page)
    final.save(out)

def main():
    if (len(sys.argv) < 4):
        print("USAGE: \'python3 croppdf.py {int : height} {file : output} {file(s): input(s)}\'")
        sys.exit(1)
    cropcat(sys.argv[3:], sys.argv[2], int(sys.argv[1]))


if __name__ == "__main__":
    main()
