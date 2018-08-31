# coding=utf-8
from collections import OrderedDict
import sys

outfile = sys.argv[1]

if outfile == "teamgrid.rst":
    team = OrderedDict([
        ("David Ham", "http://www.imperial.ac.uk/people/david.ham"),
        ("Paul Kelly", "http://www.imperial.ac.uk/people/p.kelly"),
        ("Lawrence Mitchell",
         "http://www.imperial.ac.uk/people/lawrence.mitchell"),
        ("Thomas Gibson", "http://www.imperial.ac.uk/people/t.gibson15"),
        ("Tianjiao (TJ) Sun", "https://www.hipeac.net/~tjsun/"),
        ("Miklós Homolya", "http://www.imperial.ac.uk/people/m.homolya14"),
        ("Andrew McRae", "http://people.bath.ac.uk/attm20/"),
        ("Colin Cotter", "http://www.imperial.ac.uk/people/colin.cotter"),
        ("Rob Kirby", "http://www.baylor.edu/math/index.php?id=90540"),
    ])
elif outfile == "teaminactive.rst":
    team = OrderedDict([
        ("Fabio Luporini", "http://www.imperial.ac.uk/people/f.luporini12"),
        ("Alastair Gregory", "http://www.imperial.ac.uk/people/a.gregory14"),
        ("Michael Lange", "https://www.linkedin.com/in/michael-lange-56675994/"),
        ("Simon Funke", "http://www.simonfunke.com"),
        ("Florian Rathgeber", "https://kynan.github.io"),
        ("Doru Bercea", "https://researcher.watson.ibm.com/researcher/view.php?person=ibm-Gheorghe-Teod.Bercea"),
        ("Graham Markall", "https://gmarkall.wordpress.com"),
    ])
else:
    raise ValueError("Unknown team grid: %s" % outfile)


cols = 4
colwidth = "23%"

coldashes = max(map(len, team.keys())) + 5


def separator(n):
    out.write(("-" * coldashes).join("+" * (n + 1)) + "\n")


def blank(n):
    out.write((" " * coldashes).join("|" * (n + 1)) + "\n")

out = open(outfile, "w")

out.write("..\n  This file is generated by team.py. DO NOT EDIT DIRECTLY\n")


images = []
names = []


def imagename(name):
    puny = name.split()[0].lower().encode("punycode").decode()
    return puny[:-1] if puny[-1]=="-" else puny 

# Write substitution rules for member images.
for member, url in team.items():
    out.write(".. |" + member + "| image:: /images/" +
              imagename(member) + ".*\n")
    out.write("   :width: 70%\n")
    out.write("   :target: %s\n" % url)
    out.write(".. _" + member + ": " + url + "\n")

    im = " |" + member + "|"
    images.append(im + " " * (coldashes - len(im)))
    nm = " `" + member + "`_"
    names.append(nm + " " * (coldashes - len(nm)))

out.write("\n\n")
separator(cols)

members = zip(images, names)

try:
    while True:
        irow = "|"
        nrow = "|"
        for c in range(cols):
            image, name = next(members)
            irow += image + "|"
            nrow += name + "|"

        out.write(irow + "\n")
        blank(cols)
        out.write(nrow + "\n")

        separator(cols)

except StopIteration:

    if c > 0:
        # Finish the final row.
        for rest in range(c, cols):
            irow += " " * coldashes + "|"
            nrow += " " * coldashes + "|"

        out.write(irow + "\n")
        blank(cols)
        out.write(nrow + "\n")

        separator(cols)
