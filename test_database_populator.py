import random
from database_setup import Project, Base, Student, Pref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import session as login_session
# from server.dao import (Address, Group, Person, PersonEmail, PersonPhone,
#                         User, Position, Privilege)
engine = create_engine('sqlite:///testing.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

A = Project(name='Lessons from a Student Athlete: Why the Grind Never Stops', session_number=1)
B = Project(name='Free Food!: What I learned about the LAUSDs free lunch program', session_number=2)
C = Project(name='Stories of Struggle, Victory, and Love: The Black Male Experience at Chadwick', session_number=3)
D = Project(name='Mirrors are your friend: Learning to love your body', session_number=4)
E = Project(name='AllRight: observing extreme political partisanship through FaceBook', session_number=1)
F = Project(name='A Safer E3nvironment: Chadwic3k and Mental Health', session_number=2)
G = Project(name='The Reality of the SAT/ACT', session_number=3)
H = Project(name='Emotional Abuse: A Closer Look at Pain Unseen', session_number=4)
I = Project(name='The Fifth Domain of Warfare', session_number=1)
J = Project(name='Nuclear Power: Friend or Foe?', session_number=2)
K = Project(name='Saving the Earth One Bite at a Time', session_number=3)
L = Project(name='O.E.,O.E., Never Much Love When We Go On O.E.', session_number=4)
M = Project(name='A Look into Americas Growing Health Epidemic', session_number=1)
N = Project(name='Mapping for Measles', session_number=2)
O = Project(name='A Dogs Purpose: Therapy Dogs', session_number=3)
P = Project(name='Ocean Friendly Restaurants in the South Bay', session_number=4)
Q = Project(name='Lessons from a Student Athlete: Why the Grind Never Stops', session_number=4)
R = Project(name='Triggered: What Most People Dont Know About Sports Injury', session_number=1)
S = Project(name='Spotlight: Using Childrens Theater to Enhance Multiple Intelligences', session_number=2)
T = Project(name='Bully the Bullies: The New Anti Cyberbullying Approach', session_number=3)
U = Project(name='Expanding Therapeutic Equestrian in Palos Verdes', session_number=4)
V = Project(name='Preventing Childhood Obesity in the South Bay', session_number=1)
W = Project(name='Healthy Habits To-Go: Ways to Efficiently Maintain a Balanced Lifestyle', session_number=2)
X = Project(name='Addressing the Systemic Risk of the Big Three: Depression, Anxiety, and Drug Abuse', session_number=3)
Y = Project(name='The Quality of Life in Spinal Muscular Atrophy Children', session_number=3)
Z = Project(name='Exposing the NCAA: The Rights of College Athletes', session_number=4)
AA = Project(name='AllRight: observing extreme political partisanship through FaceBook', session_number=1)
AB = Project(name='NEWSFLASH: Theater is more than just a form of entertainment', session_number=2)
AC = Project(name='Multiple Perspectives: Is my opinion really that controversial', session_number=3)
AD = Project(name='The Unshakeable Connection Between the Mind and Body', session_number=4)
AE = Project(name='Reading More Into Mental Illnesses and Homelessness: The Use of Libraries to Combat the Mentally Ill and Homeless of Long Beach', session_number=1)
AF = Project(name='Chadwick: Division 1 Sleep Deprivation', session_number=2)
AG = Project(name='The Anonymous Project', session_number=2)
AH = Project(name='Animal Advocacy: The Process of Meaningful Change', session_number=3)
AI = Project(name='A Look into the L.A. Foster Care System through Art', session_number=4)
AJ = Project(name='Eating Away at the Earth: The Meat Industrys Impact on the Environment and the Future of Meat', session_number=1)
AK = Project(name='Obesity: Quite a Large Problem if You Ask Me', session_number=2)
AL = Project(name='Stripping Away Negative Body Image: Medias Promotion of an Unattainable Ideal', session_number=3)
AM = Project(name='Blaming the Victims: The Mistreatment of Sexual Assault Cases at Educational Institutions', session_number=4)
AN = Project(name='The Spotlight Project', session_number=1)
AO = Project(name='If You Come To This Presentation, Ill Let You Nap', session_number=1)
AP = Project(name='Puzzled? Heres an Easy Way to Destress', session_number=2)
AQ = Project(name='Making Bank the Smart Way: What Chadwick Failed to Teach You', session_number=3)
AR = Project(name='Creating a Pen Pal Program to Help Orphans', session_number=4)
AS = Project(name='Houseless Not Homeless!', session_number=1)
AT = Project(name='Craving Companionship: Promoting Multigenerational Relationships to Combat Elderly Loneliness', session_number=2)
AU = Project(name='Programming Your Mind:  How To Edit Habits', session_number=3)
AV = Project(name='JAWS: Fixing Sharks Bad Reputations', session_number=4)
AW = Project(name='AllRight: observing extreme political partisanship through FaceBook', session_number=1)
AX = Project(name='Helping Hospitalized Children Cope with Stress', session_number=2)
AY = Project(name='Out of Tune: Revamping the Chadwick Instrumental Program', session_number=3)
AZ = Project(name='Solar Freakin Umbrellas: Implementing Solar Technology at Chadwick', session_number=4)
BA = Project(name='A Salute to Service Dogs', session_number=1)
BB = Project(name='Go the Frick to Sleep, You Fricking Fricks', session_number=2)
BC = Project(name='Not just a Brazilian Butt Workout: Another Type of Workout Vide', session_number=3)
BD = Project(name='Dancing in the rain during a drought: a water conservation guide for daily life', session_number=4)
BE = Project(name='From Assistants to Physicists: The Pursuit of Equality in STEM', session_number=1)
BF = Project(name='Guys And Dolls: A Look At Gendered Marketing Of Childrens Products', session_number=2)
BG = Project(name='Color Your Way Towards Happiness', session_number=3)
BH = Project(name='The California Coastline Takeover: Invasive Seaweed', session_number=4)
BI = Project(name='There Will Be Blood: Preventing Type 1 Diabetes Misdiagnosis', session_number=1)
BJ = Project(name='Stamping out Sexism in the Elementary School Classroom', session_number=2)
BK = Project(name='Capture Water Before it Goes', session_number=3)
BL = Project(name='Spotlight on the Students: Fostering Creativity in Chadwicks Stage Crew', session_number=4)
BM = Project(name='Why Should You be Grateful for Chadwick?', session_number=1)
BN = Project(name='Zoos: Born to be Wild', session_number=2)
BO = Project(name='How Many Bunnies Died for your Chapstick? Exposing Animal Testing in Cosmetics', session_number=3)
BP = Project(name='The ART of De-Stressing: Using Creativity to Promote Wellness', session_number=4)
BQ = Project(name='F#### of S####: What Can You Legally Say On Chadwicks Campus?', session_number=1)
BR = Project(name='Building Relationship with Children in Foster Care', session_number=2)
BS = Project(name='Protecting the Protected: Safeguarding Marine Protected Areas', session_number=3)
BT = Project(name='Infusing Objectivity and Individualism into Educating the Global Citizen', session_number=4)
BU = Project(name='Balancing the Numbers:  Supporting Female Engineers at Chadwick', session_number=1)
BV = Project(name='Are you a boy, girl, or other?: The importance of gender inclusion at school', session_number=2)
BW = Project(name='Empowering Girls in India Through Education', session_number=3)
BX = Project(name='Putting the Anti in Antibiotic Meat: The Pitfalls of Antibiotic Usage in Livestock Farming for Human Health and the Environment', session_number=4)
BY = Project(name='Protect Yourself Before You Wreck Yourself: The Dangers of Lifelong Sun Damage', session_number=1)
BZ = Project(name='Meditation: Methods to relieve stress and improve personal condition', session_number=2)
CA = Project(name='Fake News: the Cancer of Our Democracy', session_number=3)
CB = Project(name='What Happens To Homeless Pets In Our World', session_number=4)
CC = Project(name='Media and User Bias in the Digital Age: What You Can Do to Beat It', session_number=1)
CD = Project(name='Click on Sustainability: Reducing Your Carbon Footprint in Los Angeles', session_number=2)
CE = Project(name='Why Excessive Homework is Bad for High School Students', session_number=3)
CF = Project(name='Oh Brother!: The Conveniences and Costs of Mass Surveillance', session_number=4)
CG = Project(name='The Myth of Car Idling', session_number=1)
CH = Project(name='Need a hand? Providing a list of babysitters for families dealing with pediatric cancer', session_number=2)
CI = Project(name='"Youre So Pretty for a Black Girl": The Problem With White Beauty Ideals', session_number=3)
CJ = Project(name='Addressing Homelessness in My Community', session_number=4)
CK = Project(name='Mental Health: What do All Faculty Need to Know', session_number=1)
CL = Project(name='Healthy Habits To-Go: Ways to Efficiently Maintain a Balanced Lifestyle', session_number=2)
CM = Project(name='Addressing the Systemic Risk of the Big Three: Depression, Anxiety, and Drug Abuse', session_number=3)
CN = Project(name='The Quality of Life in Spinal Muscular Atrophy Children', session_number=4)
CO = Project(name='Kids These Days: Why Arent They Active?', session_number=1)
CP = Project(name='This Book Could Change Your Life: Combating Homophobia One Book at a Time', session_number=2)
CQ = Project(name='The Importance of Media Literacy in the Digital Age', session_number=3)
CR = Project(name='Apex under a Microscope: Employing Empathy to Ensure the Success of Chadwick Apex Projects', session_number=4)
CS = Project(name='Expanding the Admirals Role in the Chadwick Community', session_number=1)
none = Project(name='Not Matched', session_number=2)
session.add(A)
session.add(B)
session.add(C)
session.add(D)
session.add(E)
session.add(H)
session.add(I)
session.add(J)
session.add(K)
session.add(L)
session.add(M)
session.add(N)
session.add(O)
session.add(P)
session.add(Q)
session.add(R)
session.add(S)
session.add(T)
session.add(U)
session.add(V)
session.add(W)
session.add(X)
session.add(Y)
session.add(Z)
session.add(AA)
session.add(AB)
session.add(AC)
session.add(AD)
session.add(AE)
session.add(AF)
session.add(AG)
session.add(AH)
session.add(AI)
session.add(AJ)
session.add(AK)
session.add(AL)
session.add(AM)
session.add(AN)
session.add(AO)
session.add(AP)
session.add(AQ)
session.add(AR)
session.add(AS)
session.add(AT)
session.add(AU)
session.add(AV)
session.add(AW)
session.add(AX)
session.add(AY)
session.add(AZ)
session.add(BA)
session.add(BB)
session.add(BC)
session.add(BD)
session.add(BE)
session.add(BF)
session.add(BG)
session.add(BH)
session.add(BI)
session.add(BJ)
session.add(BK)
session.add(BL)
session.add(BM)
session.add(BN)
session.add(BO)
session.add(BP)
session.add(BQ)
session.add(BR)
session.add(BS)
session.add(BT)
session.add(BU)
session.add(BV)
session.add(BW)
session.add(BX)
session.add(BY)
session.add(BZ)
session.add(CA)
session.add(CB)
session.add(CC)
session.add(CD)
session.add(CE)
session.add(CF)
session.add(CG)
session.add(CH)
session.add(CI)
session.add(CJ)
session.add(CK)
session.add(CL)
session.add(CM)
session.add(CN)
session.add(CO)
session.add(CP)
session.add(CQ)
session.add(CR)
session.add(CS)
session.commit()

"""Create and add all students to database"""

# def add_student():
#     student = new_student_by_index(0)
#     with session_context(session_factory) as dbsession:
#         dbsession.add(person)

myogi = Student(first_name='myogi', matched=0)
rsullivan2020 = Student(first_name='rsullivan2020', matched=0)
mlesser2019 = Student(first_name='mlesser2019', matched=0)
ntanios2020 = Student(first_name='ntanios2020', matched=0)
kkunesh2020 = Student(first_name='kkunesh2020', matched=0)
pfreer = Student(first_name='pfreer', matched=0)
nmester2020 = Student(first_name='nmester2020', matched=0)
dgoldsmith = Student(first_name='dgoldsmith', matched=0)
wwagner2020 = Student(first_name='wwagner2020', matched=0)
jjeong2020 = Student(first_name='jjeong2020', matched=0)
dmoore2018 = Student(first_name='dmoore2018', matched=0)
carmour = Student(first_name='carmour', matched=0)
rabrahamson = Student(first_name='rabrahamson', matched=0)
atetreault2019 = Student(first_name='atetreault2019', matched=0)
anbrown = Student(first_name='anbrown', matched=0)
chobart2020 = Student(first_name='chobart2020', matched=0)
nkathuria2019 = Student(first_name='nkathuria2019', matched=0)
mchildress = Student(first_name='mchildress', matched=0)
nmester2020 = Student(first_name='nmester2020', matched=0)
gho = Student(first_name='gho', matched=0)
ajdonley = Student(first_name='ajdonley', matched=0)
skim2019 = Student(first_name='skim2019', matched=0)
glewin = Student(first_name='glewin', matched=0)
dmalone = Student(first_name='dmalone', matched=0)
etaulli = Student(first_name='etaulli', matched=0)
jmoorefield2019 = Student(first_name='jmoorefield2019', matched=0)
odulai2018 = Student(first_name='odulai2018', matched=0)
mmcgovern2020 = Student(first_name='mmcgovern2020', matched=0)
blamb2017 = Student(first_name='blamb2017', matched=0)
skrieger = Student(first_name='skrieger', matched=0)
thorne2020 = Student(first_name='thorne2020', matched=0)
cirawan = Student(first_name='cirawan', matched=0)
shingorani2020 = Student(first_name='shingorani2020', matched=0)
ssherman2020 = Student(first_name='ssherman2020', matched=0)
rhom = Student(first_name='rhom', matched=0)
tgurbach2019 = Student(first_name='tgurbach2019', matched=0)
akim = Student(first_name='akim', matched=0)
amkessaris = Student(first_name='amkessaris', matched=0)
hzilmer = Student(first_name='hzilmer', matched=0)
plane2019 = Student(first_name='plane2019', matched=0)
ggeist = Student(first_name='ggeist', matched=0)
nrizika2020 = Student(first_name='nrizika2020', matched=0)
aamberg2018 = Student(first_name='aamberg2018', matched=0)
acarter2020 = Student(first_name='acarter2020', matched=0)
jhandler2020 = Student(first_name='jhandler2020', matched=0)
jli2018 = Student(first_name='jli2018', matched=0)
miziegler = Student(first_name='miziegler', matched=0)
mwalls2020 = Student(first_name='mwalls2020', matched=0)
mwilliams2019 = Student(first_name='mwilliams2019', matched=0)
vmody = Student(first_name='vmody', matched=0)
jacastleman = Student(first_name='jacastleman', matched=0)
wburleson2020 = Student(first_name='wburleson2020', matched=0)
wburleson2020 = Student(first_name='wburleson2020', matched=0)
shurst2019 = Student(first_name='shurst2019', matched=0)
clin = Student(first_name='clin', matched=0)
atyssee2019 = Student(first_name='atyssee2019', matched=0)
asopp = Student(first_name='asopp', matched=0)
acoomans2020 = Student(first_name='acoomans2020', matched=0)
tkoo = Student(first_name='tkoo', matched=0)
kchambers = Student(first_name='kchambers', matched=0)
aeggers = Student(first_name='aeggers', matched=0)
efuire = Student(first_name='efuire', matched=0)
adavisson = Student(first_name='adavisson', matched=0)
hfgordon2019 = Student(first_name='hfgordon2019', matched=0)
jdulai2020 = Student(first_name='jdulai2020', matched=0)
jwong = Student(first_name='jwong', matched=0)
mbradshaw2019 = Student(first_name='mbradshaw2019', matched=0)
mbort = Student(first_name='mbort', matched=0)
ktrinh = Student(first_name='ktrinh', matched=0)
msood2019 = Student(first_name='msood2019', matched=0)
medwards2019 = Student(first_name='etaylor2017', matched=0)
etaylor2017 = Student(first_name='amadhani2020', matched=0)
amadhani2020 = Student(first_name='amadhani2020', matched=0)
msmith = Student(first_name='msmith', matched=0)
jconnelly2019 = Student(first_name='jconnelly2019', matched=0)
cdavodi2019 = Student(first_name='cdavodi2019', matched=0)
nanaya2017 = Student(first_name='nanaya2017', matched=0)
mdavis2017 = Student(first_name='mdavis2017', matched=0)
nnordine = Student(first_name='nnordine', matched=0)
hgordon2019 = Student(first_name='hgordon2019', matched=0)
jamaral2020 = Student(first_name='jamaral2020', matched=0)
twinter = Student(first_name='twinter', matched=0)
revans = Student(first_name='revans', matched=0)
kwhite = Student(first_name='kwhite', matched=0)
pspann = Student(first_name='pspann', matched=0)
msegal = Student(first_name='msegal', matched=0)
vranparia2020 = Student(first_name='vranparia2020', matched=0)
karoesty2018 = Student(first_name='karoesty2018', matched=0)
keu2019 = Student(first_name='keu2019', matched=0)
ksopp = Student(first_name='ksopp', matched=0)
agray2017 = Student(first_name='agray2017', matched=0)
jneill = Student(first_name='jneill', matched=0)
speri = Student(first_name='speri', matched=0)
mmasuda = Student(first_name='mmasuda', matched=0)
aablonsimpson2020 = Student(first_name='aablonsimpson2020', matched=0)
jboondicharern2020 = Student(first_name='jboondicharern2020', matched=0)
nhuh2020 = Student(first_name='nhuh2020', matched=0)
lkim2018 = Student(first_name='lkim2018', matched=0)
cbruni2020 = Student(first_name='cbruni2020', matched=0)
sgeorge = Student(first_name='sgeorge', matched=0)
jrawda2020 = Student(first_name='jrawda2020', matched=0)
avera2019 = Student(first_name='avera2019', matched=0)
jweiss2020 = Student(first_name='jweiss2020', matched=0)
cthompson2020 = Student(first_name='cthompson2020', matched=0)
jallen2018 = Student(first_name='jallen2018', matched=0)
camoskowitz = Student(first_name='camoskowitz', matched=0)
ctoups = Student(first_name='ctoups', matched=0)
gmartinez2018 = Student(first_name='gmartinez2018', matched=0)
mtchen = Student(first_name='mtchen', matched=0)
areisig2020 = Student(first_name='areisig2020', matched=0)
cpoitras = Student(first_name='cpoitras', matched=0)
mbuchanan = Student(first_name='mbuchanan', matched=0)
efukunaga = Student(first_name='efukunaga', matched=0)
rkim2020 = Student(first_name='rkim2020', matched=0)
sdegyarfas = Student(first_name='sdegyarfas', matched=0)
melliott = Student(first_name='melliott', matched=0)
bregan = Student(first_name='bregan', matched=0)
fglantz2019 = Student(first_name='fglantz2019', matched=0)
cbreus2020 = Student(first_name='cbreus2020', matched=0)
ldyson = Student(first_name='ldyson', matched=0)
ecastillo2020 = Student(first_name='ecastillo2020', matched=0)
kdoody2018 = Student(first_name='kdoody2018', matched=0)
hgoldsmith = Student(first_name='hgoldsmith', matched=0)
jyang2019 = Student(first_name='jyang2019', matched=0)
rmacquarrie2018 = Student(first_name='rmacquarrie2018', matched=0)
awhite2017 = Student(first_name='awhite2017', matched=0)
czak = Student(first_name='czak', matched=0)
gwaller = Student(first_name='gwaller', matched=0)
jwohl = Student(first_name='jwohl', matched=0)
bharrington = Student(first_name='bharrington', matched=0)
jnachman2020 = Student(first_name='jnachman2020', matched=0)
bsimpson = Student(first_name='bsimpson', matched=0)
achowdhury2019 = Student(first_name='achowdhury2019', matched=0)
amichels = Student(first_name='amichels', matched=0)
lwagner2019 = Student(first_name='lwagner2019', matched=0)
ashierbruton = Student(first_name='ashierbruton', matched=0)
cwong = Student(first_name='cwong', matched=0)
aschulten = Student(first_name='aschulten', matched=0)
thale = Student(first_name='thale', matched=0)
jbenjamin2019 = Student(first_name='jbenjamin2019', matched=0)
lproctor = Student(first_name='lproctor', matched=0)
latong = Student(first_name='latong', matched=0)
csakaguchi = Student(first_name='csakaguchi', matched=0)
dnguyen2020 = Student(first_name='dnguyen2020', matched=0)
bngan = Student(first_name='bngan', matched=0)
ggentry = Student(first_name='ggentry', matched=0)
harnett2020 = Student(first_name='harnett2020', matched=0)
choward2020 = Student(first_name='choward2020', matched=0)
sachung2019 = Student(first_name='sachung2019', matched=0)
mrenslo = Student(first_name='mrenslo', matched=0)
srivas = Student(first_name='srivas', matched=0)
mbrandmeyer = Student(first_name='mbrandmeyer', matched=0)
mmedrano2018 = Student(first_name='mmedrano2018', matched=0)
jhuh2019 = Student(first_name='jhuh2019', matched=0)
kchase2019 = Student(first_name='kchase2019', matched=0)
mbernadett2019 = Student(first_name='mbernadett2019', matched=0)
ovarady2019 = Student(first_name='ovarady2019', matched=0)
cwooten = Student(first_name='cwooten', matched=0)
nkeesey = Student(first_name='nkeesey', matched=0)
rgealer2017 = Student(first_name='rgealer2017', matched=0)
jzhang2019 = Student(first_name='jzhang2019', matched=0)
remelle2018 = Student(first_name='remelle2018', matched=0)
j5lee2020 = Student(first_name='j5lee2020', matched=0)
rfreer = Student(first_name='rfreer', matched=0)
mshah2020 = Student(first_name='mshah2020', matched=0)
jguzman2020 = Student(first_name='jguzman2020', matched=0)
clindsey2019 = Student(first_name='clindsey2019', matched=0)
mgradney2017 = Student(first_name='mgradney2017', matched=0)
hchung2020 = Student(first_name='hchung2020', matched=0)
mhuang2020 = Student(first_name='mhuang2020', matched=0)
jrand = Student(first_name='jrand', matched=0)
abaronsky = Student(first_name='abaronsky', matched=0)
cboiler2019 = Student(first_name='cboiler2019', matched=0)
ckeesey = Student(first_name='ckeesey', matched=0)
rdominguez2019 = Student(first_name='rdominguez2019', matched=0)
bbaldridge = Student(first_name='bbaldridge', matched=0)
vcho2018 = Student(first_name='vcho2018', matched=0)
jlin = Student(first_name='jlin', matched=0)
bnoble = Student(first_name='bnoble', matched=0)
gkhalil = Student(first_name='gkhalil', matched=0)
cwolf = Student(first_name='cwolf', matched=0)
kborden = Student(first_name='kborden', matched=0)
fdegiorgio2020 = Student(first_name='fdegiorgio2020', matched=0)
rcameron2019 = Student(first_name='rcameron2019', matched=0)
emirovski2020 = Student(first_name='emirovski2020', matched=0)
hgoodloe = Student(first_name='hgoodloe', matched=0)
ntell2019 = Student(first_name='ntell2019', matched=0)
wzheng2019 = Student(first_name='wzheng2019', matched=0)
tshim2018 = Student(first_name='tshim2018', matched=0)
eshaw2019 = Student(first_name='eshaw2019', matched=0)
sbarry2020 = Student(first_name='sbarry2020', matched=0)
shughes2020 = Student(first_name='shughes2020', matched=0)
mdinnegan = Student(first_name='mdinnegan', matched=0)
mrosenzweig2018 = Student(first_name='mrosenzweig2018', matched=0)
jkole2017 = Student(first_name='jkole2017', matched=0)
rkennedy = Student(first_name='rkennedy', matched=0)
azhou2018 = Student(first_name='azhou2018', matched=0)
ggay2018 = Student(first_name='ggay2018', matched=0)
lhill2019 = Student(first_name='lhill2019', matched=0)
arosso2019 = Student(first_name='arosso2019', matched=0)
mhodgkiss2019 = Student(first_name='mhodgkiss2019', matched=0)
ccastagne = Student(first_name='ccastagne', matched=0)
miadimson2019 = Student(first_name='miadimson2019', matched=0)
ahe2018 = Student(first_name='ahe2018', matched=0)
swchung2019 = Student(first_name='swchung2019', matched=0)
abagabo2020 = Student(first_name='abagabo2020', matched=0)
jsoldera = Student(first_name='jsoldera', matched=0)
cspennato = Student(first_name='cspennato', matched=0)
mpacifico2018 = Student(first_name='mpacifico2018', matched=0)
asimpson = Student(first_name='asimpson', matched=0)
amitchell = Student(first_name='amitchell', matched=0)
skrasne = Student(first_name='skrasne', matched=0)
bbrown = Student(first_name='bbrown', matched=0)
joberenato = Student(first_name='joberenato', matched=0)
amoyabeck = Student(first_name='amoyabeck', matched=0)
nlonghurst = Student(first_name='nlonghurst', matched=0)
hlennertz2020 = Student(first_name='hlennertz2020', matched=0)
jheisler2020 = Student(first_name='jheisler2020', matched=0)
csmith = Student(first_name='csmith', matched=0)
rkocarslan2017 = Student(first_name='rkocarslan2017', matched=0)
sjung2018 = Student(first_name='sjung2018', matched=0)
amenzelos2017 = Student(first_name='amenzelos2017', matched=0)
trizika2017 = Student(first_name='trizika2017', matched=0)
cproctor = Student(first_name='cproctor', matched=0)
aberenato = Student(first_name='aberenato', matched=0)
mkripalani2017 = Student(first_name='mkripalani2017', matched=0)
rning = Student(first_name='rning', matched=0)
hkoontz2017 = Student(first_name='hkoontz2017', matched=0)
aelliott2017 = Student(first_name='aelliott2017', matched=0)
edavis = Student(first_name='edavis', matched=0)
aschwake2019 = Student(first_name='aschwake2019', matched=0)
jfranklin2020 = Student(first_name='jfranklin2020', matched=0)
bclaird2019 = Student(first_name='bclaird2019', matched=0)
akirkpatrick = Student(first_name='akirkpatrick', matched=0)
hfreni = Student(first_name='hfreni', matched=0)
kcorbalis = Student(first_name='kcorbalis', matched=0)
rmack = Student(first_name='rmack', matched=0)
jdoi = Student(first_name='jdoi', matched=0)
garcangeli2020 = Student(first_name='garcangeli2020', matched=0)
gthomas2020 = Student(first_name='gthomas2020', matched=0)
odalton2018 = Student(first_name='odalton2018', matched=0)
awestley2017 = Student(first_name='awestley2017', matched=0)
saliu2020 = Student(first_name='saliu2020', matched=0)
cwallace2017 = Student(first_name='cwallace2017', matched=0)
sbernstein2020 = Student(first_name='sbernstein2020', matched=0)
nbogert = Student(first_name='nbogert', matched=0)
jmerkin = Student(first_name='jmerkin', matched=0)
habruni = Student(first_name='habruni', matched=0)
camihm = Student(first_name='camihm', matched=0)
jalexander2018 = Student(first_name='jalexander2018', matched=0)
khuibonhoa = Student(first_name='khuibonhoa', matched=0)
kchappell2019 = Student(first_name='kchappell2019', matched=0)
phuibonhoa = Student(first_name='phuibonhoa', matched=0)
sreeves2020 = Student(first_name='sreeves2020', matched=0)
ahale2020 = Student(first_name='ahale2020', matched=0)
kgoy2020 = Student(first_name='kgoy2020', matched=0)
pelliott2020 = Student(first_name='pelliott2020', matched=0)
itaulli = Student(first_name='itaulli', matched=0)
mabad2020 = Student(first_name='mabad2020', matched=0)
mgood2017 = Student(first_name='mgood2017', matched=0)
ncorrea2020 = Student(first_name='ncorrea2020', matched=0)
jamesagnew = Student(first_name='jamesagnew', matched=0)
thwang2018 = Student(first_name='thwang2018', matched=0)
kgarrett = Student(first_name='kgarrett', matched=0)
astary = Student(first_name='astary', matched=0)
ofoster = Student(first_name='ofoster', matched=0)
ncoomans2020 = Student(first_name='ncoomans2020', matched=0)
nfox2020 = Student(first_name='nfox2020', matched=0)
tritter = Student(first_name='tritter', matched=0)
cyoon2019 = Student(first_name='cyoon2019', matched=0)
jhoot2018 = Student(first_name='jhoot2018', matched=0)
jaroesty2019 = Student(first_name='jaroesty2019', matched=0)
epark2020 = Student(first_name='epark2020', matched=0)
msung2019 = Student(first_name='msung2019', matched=0)
efoster = Student(first_name='efoster', matched=0)
aradell2018 = Student(first_name='aradell2018', matched=0)
cfrey2019 = Student(first_name='cfrey2019', matched=0)
ereisig2017 = Student(first_name='ereisig2017', matched=0)
jchao = Student(first_name='jchao', matched=0)
fharmon = Student(first_name='fharmon', matched=0)
esiddons2020 = Student(first_name='esiddons2020', matched=0)
hwatson2018 = Student(first_name='hwatson2018', matched=0)
dding2018 = Student(first_name='dding2018', matched=0)
dsuh = Student(first_name='dsuh', matched=0)
sbeshke = Student(first_name='sbeshke', matched=0)
tjoshi = Student(first_name='tjoshi', matched=0)
nlinden = Student(first_name='nlinden', matched=0)
pcarter = Student(first_name='pcarter', matched=0)
dbishop2018 = Student(first_name='dbishop2018', matched=0)
sbogen2019 = Student(first_name='sbogen2019', matched=0)
dhoule = Student(first_name='dhoule', matched=0)
tgurbach2019 = Student(first_name='tgurbach2019', matched=0)
abuchanan = Student(first_name='abuchanan', matched=0)
kwhite = Student(first_name='kwhite', matched=0)
szukerman2017 = Student(first_name='szukerman2017', matched=0)
nrizika2020 = Student(first_name='nrizika2020', matched=0)
rgracie = Student(first_name='rgracie', matched=0)
caxtell2017 = Student(first_name='caxtell2017', matched=0)
slevy = Student(first_name='slevy', matched=0)
vangelow2019 = Student(first_name='vangelow2019', matched=0)
msmith = Student(first_name='msmith', matched=0)
alcoward = Student(first_name='alcoward', matched=0)
istamos = Student(first_name='istamos', matched=0)
sbernstein2020 = Student(first_name='sbernstein2020', matched=0)
tpeters2019 = Student(first_name='tpeters2019', matched=0)
edevaughn = Student(first_name='edevaughn', matched=0)
ecortez2020 = Student(first_name='ecortez2020', matched=0)
akim2020 = Student(first_name='akim2020', matched=0)
chobart2020 = Student(first_name='chobart2020', matched=0)
cchang = Student(first_name='cchang', matched=0)
clenihan = Student(first_name='clenihan', matched=0)
nbenson = Student(first_name='nbenson', matched=0)
mcorley2017 = Student(first_name='mcorley2017', matched=0)
