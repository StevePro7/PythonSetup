README 04
03-Jun-2026

adriana

01. Sound
Linux got ["Dummy Output] so initial check pass when should have failed
then fails when load sound SFX - need to make more robust


02. Title
Need to get build version DrawText() not TextList


03. Sound test all APIs


04. Content Mgr
do I need FontMgr - maybe load all content via Content Mgr??


05. Colors
e.g. Display Mgr


06. DRY
QM
TM
def __getTextFile(self, textFile: str) -> str:


07. public Question LoadQuestion(Byte index)
as we cannot override methods - I renamed this PlayQuestion
which is used in PlayScreen


08. Init screen - prints black text on black background
Do I want a toggle where white text on black or vice versa?


IMPORTANT
OptionType
original code uses None but cannot be used in Python
so I renamed to Invalid
