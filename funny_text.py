import random
import csv
from collections import defaultdict
import time

def rword(x):
    """Used to generate random integers for name selection and word gen."""
    count = 0
    for i in x:
        count += 1
    rnumber = random.randint(0,count - 1)
    return rnumber
# random names initialization
def rname():
    columns = defaultdict(list) # each value in each column is appended to a list
    with open('app_c.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value
                columns[k].append(v) # append the value into the appropriate list
                                    # based on column name k
    return columns['name']

# initialize lists from files
nouns = list(open("nouns.txt").read().splitlines())
verbs = list(open("verbs.txt").read().splitlines())
adjectives = list(open("adjectives.txt").read().splitlines())
adverbs = list(open("adverbs.txt").read().splitlines())
departments = ["HR","R&D","IT","Management","QA"]

quit = False
name_list = rname()

# fun little doo-hickey
x = input("Hello, this is Han's automatic email checker. \nPlease enter your email."
)
print("Email confirmed. Accessing...")
time.sleep(2)
x = input("Email authentification complete. You have one new message.\nWould you like to view?")
print("Opening...")
time.sleep(1)

while quit == False:
    name = name_list[rword(name_list)]
    name2 = name_list[rword(name_list)]
    textselect = random.randint(0,3)
    departmentselect = departments[random.randint(0,4)]
    if textselect == 0:

        print("""Hi %s,\n
Take a step back and let's %s the %s. What really happened? As I recall it was a serious breakdown in %s.
We should %s this and %s for the consumer! Call %s and tell them to %s and we'll %s with %s.
We've got to %s %s to get all this sorted out.
\nBest, \n %s"""%(name,verbs[rword(verbs)],nouns[rword(nouns)],nouns[rword(nouns)],
verbs[rword(verbs)],verbs[rword(verbs)],departmentselect,verbs[rword(verbs)], verbs[rword(verbs)],
nouns[rword(nouns)],verbs[rword(verbs)], adverbs[rword(adverbs)],name2))
    elif textselect == 1:
        print("""Thanks %s. I can always count on you to %s on our core substrates.
        You have a real knack for %s, and I admire your customer obsession. We should %s this %s
        to allow our partners to %s more, and take the opportunity to improve our %s. Let's %s it for now; we can %s later. If you
        have the cycles, %s to the %s and see if there is room for %s. Again, great work.
        We're standing on the shoulders of giants here.
        Best, %s"""%(name,verbs[rword(verbs)],nouns[rword(nouns)],verbs[rword(verbs)],nouns[rword(nouns)],
        verbs[rword(verbs)],nouns[rword(nouns)],
        verbs[rword(verbs)],verbs[rword(verbs)],verbs[rword(verbs)],departmentselect,nouns[rword(nouns)],name2))
    elif textselect ==2:
        print("""Hi %s,
        Glad my earlier message struck a chord with you. Allowing people to %s beyond expectations and achieving %s is what makes this role great.
        Feel free to %s with me any time you'd like, I'd be happy to do a %s. Let's %s together.
        Best,
        %s"""%(name,verbs[rword(verbs)],nouns[rword(nouns)],verbs[rword(verbs)],nouns[rword(nouns)],verbs[rword(verbs)],name2))
    elif textselect ==3:
        print("""Hey %s,
        It seems like we're not in rhythm but I'm %s about the %s you're bringing here. If we %s and
        %s I'm sure we can manage to %s this while leveraging a %s to %s for all shareholders.
        Talk later,
        %s
        """%(name,adjectives[rword(adjectives)],nouns[rword(nouns)],verbs[rword(verbs)],verbs[rword(verbs)],verbs[rword(verbs)],
        nouns[rword(nouns)],verbs[rword(verbs)],name2))
    x = input("Generate another text? Press x to quit.")
    if x == "x":
        quit = True

text1 = """Look, take a step back and let's avoid the water cooler. talk.
What really happened? As I recall it was a serious breakdwon in communication. We should
do as the Romans do and realign our message with what the consumer wants! Call R&D and tell
them to buckle down on some new ideas and we'll place them on the vision board
for the next meeting with the shareholders. We've got till T minus 12pm to get all
this sorted out."""

text2 = """Thanks James. I can always count on you to drive laser focus on our core
substrates. You have a real knack for delivering success, and I admire your customer
obsession. We should leverage this data to empower our partners to achieve more, and raise
consumption and revenue. Let's table this for now; we can double click into it later. If
you have the cycles, reach out to the account manager and see if there is room for
an on site engagement. Again, great work. We're standing on the shoulders of giants here."""

text3 = """Glad my earlier message struck a chord with you. Empowering our customers to exceed
expectations on their key deliverables is what makes this role great. Grab 30 min on my
calender any time you'd like, I'd be happy to do a deep dive on this. Let's build
something great together."""

text4 = """It seems like we're not in rhythm but I'm jazzed about the energy you're
bringing here. If we avoid the low hanging fruit and redirect I'm sure we can
manage to 80/20 this while affording a synergistic solution to bring a W for all shareholders."""
