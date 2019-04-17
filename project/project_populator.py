"""Python file to populate database with project data from 2019"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Pref, Project

# ENGINE = create_engine('mysql+pymysql://chadwick:godolphins@apex-matching.c0plu8oomro4.us-east-2.rds.amazonaws.com:3306/testdb')
# ENGINE = create_engine('sqlite:///database.db')
# ENGINE = create_engine('mysql+pymysql://chadwick:godolphins@apex-matching2.c0plu8oomro4.us-east-2.rds.amazonaws.com:3306/production')

ENGINE = create_engine('mysql+pymysql://chadwick:godolphins@apex-matching16.c0plu8oomro4.us-east-2.rds.amazonaws.com:3306/production')

Base.metadata.bind = ENGINE
DBSESSION = sessionmaker(bind=ENGINE)
session = DBSESSION()

# Session 1 Projects
A = Project(name='Identity Theft Is Not a Joke, Jim!: Why Millions of Families Suffer Every Year: David Malone', session_number=1)
B = Project(name='The True Price of a College Education: The Crippling Long-Term Effects of Student Loans: Jessie Doty', session_number=1)
C = Project(name='E-cigarettes: An Adolescent Epidemic: Eugene Moon', session_number=1)
D = Project(name='Can\'t Sit Still? You\'re Not Alone ... And It\'s Not Entirely Your Fault: Morgan Brandmeyer', session_number=1)
E = Project(name='Making a Man: Toxic Masculinity: Alex Rosso', session_number=1)
F = Project(name='Our Mighty Mascot, the Bottlenose Dolphin: The Flaws in our Recycling Habits: Macy Dimson', session_number=1)
G = Project(name='We\'re Human, Too: Combatting Anti-Semitism in the Los Angeles Area: Sam Bogen', session_number=1)
H = Project(name='I Hate Chadwick: Unpacking and Addressing Negativity Among the Student Body: Lizzie Davis', session_number=1)
I = Project(name='Plugging Into the Future: Electric Vehicle Charging at Chadwick: C.B. Frey', session_number=1)
J = Project(name='Bunnies are Beautiful Without Makeup: Animal Testing of Cosmetics: Mary Bernadett', session_number=1)
K = Project(name='Save the Bees of Manhattan Beach: Tucker Hale', session_number=1)
L = Project(name='#WhatIsYourBodyImage?: Caitlin Wolf', session_number=1)
M = Project(name='Mental Health and Entertainment: A Beneficial Correlation: Nick Tell', session_number=1)
N = Project(name='Sex Ed Isn\'t Just for Heterosexuals: Creating a More Inclusive Sexual Health Curriculum for All Students: Margot Bradshaw', session_number=1)
O = Project(name='Students on the Spectrum in College: How to Help Them Succeed: Jonathan Wohl', session_number=1)
P = Project(name='To Not Partake in the \"Ted Bundy is Hot\" Movement: Shannon Chung', session_number=1)
Q = Project(name='Clean Up, Clean Up, Every Dolphin Everywhere: The Clean Chadwick Challenge: Mike Hodgkiss', session_number=1)
R = Project(name='Every Student, Every Day: Utilizing Leadership to Cure Chronic Absenteeism: Alexa Schwake', session_number=1)
S = Project(name='The Growing Problem of Invasive Species: How America\'s Natural Resources Are Being Eaten Alive: Bryan Regan', session_number=1)
T = Project(name='Creating Young Artists: Bringing Art Back to Schools: Klark White', session_number=1)
U = Project(name='Why \"Red vs. Blue\" Becomes \"Me vs. You\": Aidan Tyssee', session_number=1)
V = Project(name='Shatter the Stigma: Normalizing Mental Health Conversations: Allison Coward', session_number=1)
W = Project(name='Is College An Option For All Of Us?: Latinos In Higher Education: Sam Rivas', session_number=1)
X = Project(name='Ryan\'s Guide to Succeeding at Work: Ryan Hom', session_number=1)

# Session 2 Projects
Y = Project(name='Our Trash: Chloe Lin', session_number=2)
Z = Project(name='Water ... a Right or a Privilege?: Lead in LAUSD Schools\' Water: Jack Connelly', session_number=2)
AA = Project(name='Are You Depressed?: Making Long-Term Treatment Accessible to the Chadwick Community: Katie Eu', session_number=2)
AB = Project(name='Political Polarization: It\'s Not Black and White-It\'s Red and Blue: Jordan Yang', session_number=2)
AC = Project(name='Human Rights. Period: Why Everyone Should Have Access to Feminine Care Products: Alex Davisson', session_number=2)
AD = Project(name='Clash of Cultures: How Americans Find Their Cultural Identity: Race Cameron', session_number=2)
AE = Project(name='Is Chadwick a \"Rich Kid\" School?: Lack of Discussion around Socioeconomic Class in Elite Independent Schools: Vetta Angelow', session_number=2)
AF = Project(name='MAST: Fighting Human Trafficking at Sea: Caden Moskowitz', session_number=2)
AG = Project(name='There is no Plan(et) B: Fostering Student Leadership through Environmental Stewardship in K-12 Schools as the Future of Education: Taryn Gurbach', session_number=2)
AH = Project(name='Turning Streetwear into Progress: The Importance of Being Socially Responsible: Jeffrey Zhang', session_number=2)
AI = Project(name='Everyone Hate$ the College Board: The $truggle with Inequity in the College Proce$$: Marin Tchen', session_number=2)
AJ = Project(name='Sleep Deprivation: A Modern Epidemic: Cameron Davodi', session_number=2)
AK = Project(name='A Quiet Place: Creating Silent Study Environments for Students: Mia Dimson', session_number=2)
AL = Project(name='The Black Truth: A Black Student\'s Perspective at Chadwick: Duke Lindsey', session_number=2)
AM = Project(name='Legalized Animal Cruelty?: The Complexities of the Animal Agricultural Industry: Julia Moorefield', session_number=2)
AN = Project(name='Just Flip That Switch! Reducing Chadwick\'s Energy Consumption: Grant Ho', session_number=2)
AO = Project(name='6 Figures in 15 Minutes: Smart Financial Education for the Future: Neville Linden', session_number=2)
AP = Project(name='The Stories We Tell Ourselves: A Linguistic Review of Youth Mental Health Decline: Kate Borden', session_number=2)
AQ = Project(name='Dance Dance Revolution: Dance\'s Impact on Athletic Performance: KC Chambers', session_number=2)
AR = Project(name='The Sixth Extinction: How It Affects Insects: Brodrick Laird', session_number=2)
AS = Project(name='Stitching Up the Cultural Gap: How to Improve Low-Income Patient Experience: Amber Zheng', session_number=2)
AT = Project(name='Is Literature LIT?: Implementing Pleasure Reading Into the English Curriculum: Anandi Choudhury', session_number=2)

# Session 3 Projects
AU = Project(name='Communicating Pressure and Depression: Luke Wagner', session_number=3)
AV = Project(name='Tiny but Mighty: How Secondary Microplastics Affect the Environment, the U.S. Economy, and Human Health: Olivea Varady', session_number=3)
AW = Project(name='Staying Up All Night: The Problem With Procrastination in Teens: Robert Dominguez', session_number=3)
AX = Project(name='\"STORYTIME! An Entire Industry Mistook Me for a Man\": A Female Athletic Wear Epidemic: Rane Zilmer', session_number=3)
AY = Project(name='Why \"Red vs. Blue\" Becomes \"Me vs. You\": Tommy Peters', session_number=3)
AZ = Project(name='Starving for a Solution: The L.A. Food Desert Problem: Josie Benjamin', session_number=3)
BA = Project(name='Scandals, Suicide, and Drugs: Unhealthy Stress in Standardized Testing: Mitchell Masuda', session_number=3)
BB = Project(name='Growing Grit and Thriving through the Storm: Hannah Harris', session_number=3)
BC = Project(name='A Year With a Bum Stomach: A Zach Goodman Story: Zach Goodman', session_number=3)
BD = Project(name='Ban Shark Finning: Fish Are Friends, NOT Food!: Annamaria Berenato', session_number=3)
BE = Project(name='Paint the Streets Gold: Drawing a New Life for Minority Students from Low-Income Neighborhoods: Adrian Vera', session_number=3)
BF = Project(name='Learning to "See More and Be More": Body Image Education in Chadwick Middle School: Brooke Simpson', session_number=3)
BG = Project(name='Water ... a Right or a Privilege?: Lead in LAUSD School\'s Water: Bronson Laird', session_number=3)
BH = Project(name='Free Speech: A Clear and Present Danger?: Sophia George', session_number=3)
BI = Project(name='Aerobic Fitness Solves America\'s Problem With Screens: Matt Lesser', session_number=3)
BJ = Project(name='The Next-door Neighbors We Didn\'t Ask For: Hailie Goldsmith', session_number=3)
BK = Project(name='The Invisible Student: Introverts in the Classroom: Alden Tetreault', session_number=3)
BL = Project(name='No Forgotten Children: Overcoming the Educational Barriers for Students in Tanzania: Hannah Gordon', session_number=3)
BM = Project(name='You Can Help Yourself While Helping Others: Charlie Boiler', session_number=3)
BN = Project(name='Make Thrifted Gucci the New Standard: The Dangers of Fast Fashion: Stephanie Kim', session_number=3)
BO = Project(name='Diversity in Chadwick\'s Faculty: A Closer Look at Hiring: Kaylen Chase', session_number=3)
BP = Project(name='"Are People an Invasive Species?": The Impact of Tourism on the North Shore of Oahu: Lily Hill', session_number=3)
BQ = Project(name='Patrick Spanns Apex Presentation', session_number=3)

# Session 4 Prjects
BR = Project(name='Where Do You Belong?: Finding Home at Chadwick: Samantha de Gyarfas', session_number=4)
BS = Project(name='Travel Far and Wide: Solving the Problem of Affording Chadwick Trips: Mateus Edwards', session_number=4)
BT = Project(name='Without PRESSedent: The White House vs. A Free Press: Jenny Huh', session_number=4)
BU = Project(name='The Lack of Public Bathroom Access on Skidrow: Skyler Phinney', session_number=4)
BV = Project(name='Stopping Cyclical Stress: What Every High School Student Needs to Know: Katie Garrett', session_number=4)
BW = Project(name='Paradise or Plantation?: The Ecotourism Dilemma: Troy Dillon', session_number=4)
BX = Project(name='Smells Like Green Spirit: A Movement Towards Compostable Products in the Cafeteria: Manasi Movva', session_number=4)
BY = Project(name='Immortality or Extinction: The Journey to Superintelligence: Tej Joshi', session_number=4)
BZ = Project(name='Educator or Friend?: Why Strong Student-teacher Relationships Are Crucial to the High School Experience: Christine Zak', session_number=4)
CA = Project(name='Project YES: Youth Educational Support within LAUSD: Gibran Khalil', session_number=4)
CB = Project(name='Make Thrifted Gucci the New Standard: The Dangers of Fast Fashion: Christy Yoon', session_number=4)
CC = Project(name='Compose Yourself!: Celebrating Artistic Creativity and its Impact on the Community: Samuel Chung', session_number=4)
CD = Project(name='Art Behind Bars: Connecting with Prisoners through Artwork: Ana Michels', session_number=4)
CE = Project(name='Underage Drinking: How Bad Can It Be?: Patrick Lane', session_number=4)
CF = Project(name='\"No, You Hold the Crying Baby\": Gender Equality in the Home: Katie Shaw', session_number=4)
CG = Project(name='How Harmful Are Drugs?: Building Your Own Perspective: Frank Glantz', session_number=4)
CH = Project(name='How Meaningful Social/Emotional Curriculums Can Help Decrease Anxiety in Elementary School Students: Emily Shaw', session_number=4)
CI = Project(name='Childhood Obesity: Preventing an Epidemic: Nikhil Kathuria', session_number=4)
CJ = Project(name='Asians Don\'t Care about Mental Health: Maia Sung', session_number=4)
CK = Project(name='Water, Water, Everywhere, But Not a Drop to Drink: Spencer Hurst', session_number=4)
CL = Project(name='You Live in a Kill-Zone. Here\'s What You Can Do About It: Kate Chappell', session_number=4)
CM = Project(name='Shop with Your Soul: A Beginner\'s Guide to Meat and Dairy Labels: Lauren Thomson', session_number=4)
CN = Project(name='An Irrational Number: Addressing the Disproportionate Female Representation in Mathematical Fields: Megan Dinnegan', session_number=4)

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
session.commit()
