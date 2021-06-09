from django.db import models

CHOICE = (
    ('RVCE', 'RVCE'),
    ('BMS', 'BMS')
)
EVENTOPTION=(
    ('Adjunct Faculty','Adjunct Faculty'),
    ('Board of Studies','Board of Studies'),
    ('Carrer Journey/Leadership','Carrer Journey/Leadership'),
    ('College Relationship Manager','College Relationship Manager'),
    ('Conference','Conference'),
    ('Contest','Contest'),
    ('Curriculum Review','Curriculum Review'),
    ('Demo','Demo'),
    ('Faculty Development Program','Faculty Development Program'),
    ('Global Remote Mentoring','Global Remote Mentoring'),
    ('Guest Lecture','Guest Lecture'),
    ('Hackathon','Hackathon'),
    ('Industry visit','Industry visit'),
    ('Tech Fest','Tech Fest'),
    ('KOL Webinar','KOL Webinar'),
    ('Workshop','Workshop')

)
TRACKSOPTION=(
    ('Across Technologies','Across Technologies'),
    ('Agile/DevOps','Agile/DevOps'),
    ('Blockchain','Blockchain'),
    ('Cloud','Cloud'),
    ('Data Science(AI/ML/Analytics/NLP)','Data Science(AI/ML/Analytics/NLP)'),
    ('Design Thinking','Design Thinking'),
    ('IOT','IOT'),
    ('Mainframe','Mainframe'),
    ('Patents/IP','Patents/IP'),
    ('Platform/Database','Platform/Database'),
    ('Programming/Engineering','Programming/Engineering'),
    ('Quantum Computing','Quantum Computing'),
    ('Security','Security')

)
EVENTOPTION=(
    ('Online/Webinar','Online/Webinar'),
    ('On Campus/ In person','On Campus/ In person')
)
BOOLEANOPTION=(
    ('YES','YES'),
    ('NO','NO')
)
ORGANISEDOPTION=(
    (
        ('IBM','IBM'),
        ('College','College'),
        ('ACM','ACM'),
        ('ICDMAI','ICDMAI'),
        ('IEEE','IEEE'),
        ('NPTEL','NPTEL'),
        ('PALS','PALS')

    )
)
BUOPTION=(
    ('GBS','GBS'),
    ('GTS','GTS'),
    ('HR','HR'),
    ('IRL','IRL'),
    ('ISDL','ISDL'),
    ('ISL','ISL'),
    ('Security','Security'),
    
)
URSPOCOPTION=(
    ('Khundmir Syed','Khundmir Syed'),
    ('Mani Madhukar','Mani Madhukar'),
    ('Mona Bharadwaj','Mona Bharadwaj'),
    ('Poornima Iyengar','Poornima Iyengar')
)
STATUSOPTION=(
    ('Planned','Planned'),
    ('Completed','Completed'),
    ('Approved','Approved'),
    ('Rejected','Rejected')
    )
COLLEGEOPTION=(
    ('Platinum','Platinum'),
    ('Other','Other')
)
SESSIONOPTION=(
('1','1'),
('2','2'),
('3','3'),
('4','4'),
('5','5'),
('6','6'),
('7','7'),
('8','8')
)
class Event(models.Model):
 
    Ambassodor=models.CharField(max_length=500, choices=BOOLEANOPTION, blank=True)
    Date=models.DateTimeField(blank=True, null=True)
    Quarter= models.IntegerField(default=4, null=True, blank=True)
    EventActivityType=models.CharField(max_length=500, choices=EVENTOPTION, null=True, blank=True)
    TechnologyTracks=models.CharField(max_length=500, choices=TRACKSOPTION, null=True, blank=True)
    EventActivityMode=models.CharField(max_length=500, choices=EVENTOPTION, null=True, blank=True)
    OrganisedBy=models.CharField(max_length=500, choices=ORGANISEDOPTION, null=True, blank=True)
    SessionDuration=models.CharField(max_length=500, choices=SESSIONOPTION, null=True, blank=True)
    SMEBU=models.CharField(max_length=500, choices=BUOPTION, null=True, blank=True)
    URSPOC=models.CharField(max_length=500, choices=URSPOCOPTION, null=True, blank=True)
    Status=models.CharField(max_length=500, choices=STATUSOPTION, null=True, blank=True)
    CollegeCategory=models.CharField(max_length=500, choices=COLLEGEOPTION, null=True, blank=True)
    def __str__(self):
        return self.name
