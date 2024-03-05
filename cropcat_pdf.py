import argparse
import pikepdf
import sys

def cropcat(inp, out, height):
    final = pikepdf.Pdf.new()
    for pdf in inp:
        curr = pikepdf.open(pdf)
        for page in curr.pages:
            page.MediaBox[1] += height
            final.pages.append(page)
    final.save(out)

def main():
    if (len(sys.argv) < 4):
        print("Need <height> <output> <inputs...>")
        sys.exit(1)
    cropcat(sys.argv[3:], sys.argv[2], int(sys.argv[1]))


if __name__ == "__main__":
    main()
