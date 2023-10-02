import polib

files = ["admin","author","default","editor","emails","locale","manager","manager","submission"]

for file in files:
    fa_pofile = polib.pofile(f'locale/fa/{file}.po')
    en_pofile = polib.pofile(f'locale/en/{file}.po')

    for entry in fa_pofile:
        if entry.msgstr == "":
            en_found = en_pofile.find(entry.msgid)
            # print(entry.msgid, en_found.msgstr if en_found else None)
            if en_found:
                entry.msgstr = en_found.msgstr
    fa_pofile.save()
    print(f'file {file} done')