from tgbot.core.models import *

langs = ["Английский", "Китайский"]
themes = ["Еда", "Путешествия", "Семья", "Свободная"]
levels = ["HSK", "A", "B", "C"]

# for lg in langs:
#     row = Language(
#         name=lg+" язык"
#     )
#     row.save()
#
# for th in themes:
#     row = Theme(
#         name=th
#     )
#     row.save()

for lvl in levels:
    if lvl == "HSK":
        lang = Language.get(Language.name == "Китайский язык")
        for i in range(1, 10):
            row = LanguageLevel(
                name=lvl+" "+str(i),
                lang_id=lang
            )
            row.save()

    elif lvl == "A":
        lang = Language.get(Language.name == "Английский язык")
        for i in range(1, 3):
            row = LanguageLevel(
                name=lvl + str(i),
                lang_id=lang
            )
            row.save()

    elif lvl == "B":
        lang = Language.get(Language.name == "Английский язык")
        for i in range(1, 3):
            row = LanguageLevel(
                name=lvl + str(i),
                lang_id=lang
            )
            row.save()

    elif lvl == "C":
        lang = Language.get(Language.name == "Английский язык")
        for i in range(1, 3):
            row = LanguageLevel(
                name=lvl + str(i),
                lang_id=lang
            )
            row.save()
