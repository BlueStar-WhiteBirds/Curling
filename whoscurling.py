#!python3
import os, sys
from os.path import join
import csv as csvlib
class MEMBER:
    def __init__(self,first_name,last_name,email,phone,membership,choices,experience,comments,emcontact,emphone):
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email
        self.phone      = phone
        self.membership = membership
        self.choices    = choices
        self.experience = experience
        self.comments   = comments
        self.emcontact  = emcontact
        self.emphone    = emphone
    def print_info(self):
        print("%s %s, %s, %s, %s, %s, %s, %s, %s"%(self.first_name,self.last_name,self.email,self.phone,self.membership,self.experience,self.comments,self.emcontact,self.emphone))
        
def get_members(members,day):
    print ("Name, Email, Phone, Membership type, Experience, Comments, Emergency Contact, Emergency Phone")
    for member in members:
        #Unlimited members
        if ("U" in member.membership and day in member.choices):
            member.print_info()
        #2 leagues members
        if ("2-" in member.membership and day in member.choices[0:2]):
            member.print_info()
        #1 league members
        if ("1-" in member.membership and day in member.choices[0]):
            member.print_info()
    
def parse_csv(file,day):
    lines = []
    with open(file,'r') as f:
        for line in f:
            lines.append(line)
    csv    = list(csvlib.reader(lines, delimiter=',', quotechar='"', skipinitialspace=True))[1:]
    header = list(csvlib.reader(lines, delimiter=',', quotechar='"', skipinitialspace=True))[0]
    headerIndex = {}
    for heading in header:
        headerIndex[heading] = header.index(heading)
    members = []
    for line in csv:
        last_name  = line[headerIndex["LAST NAME"]]
        first_name = line[headerIndex["FIRST NAME"]]
        email      = line[headerIndex["EMAIL"]]
        phone      = line[headerIndex["PRIMARY PHONE"]]
        membership = line[headerIndex["INITIAL MEMBERSHIP"]]
        choices    = []
        if (line[headerIndex["1ST LEAGUE CHOICE"]].strip() != ''):
            choices.append(line[headerIndex["1ST LEAGUE CHOICE"]].strip())
            if (line[headerIndex["2ND LEAGUE CHOICE"]].strip() != ''):
                choices.append(line[headerIndex["2ND LEAGUE CHOICE"]].strip())
                if (line[headerIndex["3RD LEAGUE CHOICE"]].strip() != ''):
                    choices.append(line[headerIndex["3RD LEAGUE CHOICE"]].strip())
                    if (line[headerIndex["4TH LEAGUE CHOICE"]].strip() != ''):
                        choices.append(line[headerIndex["4TH LEAGUE CHOICE"]].strip())
                        if (line[headerIndex["5TH LEAGUE CHOICE"]].strip() != ''):
                            choices.append(line[headerIndex["5TH LEAGUE CHOICE"]].strip())
        experience            = line[headerIndex["EXPERIENCE"]]
        comments              = line[headerIndex["COMMENTS"]]
        emcontact             = line[headerIndex["EMERGENCY CONTACT NAME"]]
        emphone               = line[headerIndex["EMERGENCY NUMBER"]]
        members.append(MEMBER(first_name,last_name,email,phone,membership,choices,experience,comments,emcontact,emphone))
    get_members(members,day)
        
def main():
    if (len(sys.argv) < 3):
        print ("Provide the member sign up csv and the day to look at")
        print ("python3 whoscurling.py <the downloaded csv from gsheet> <The day of choice>")
        print ("e.g. python3 whoscurling.py curling_registration.csv M")
        sys.exit(1)
    else:
        parse_csv(sys.argv[1], sys.argv[2])
    
if __name__ == "__main__":
    main()
