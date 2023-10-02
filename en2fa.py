import polib

files = ["admin","author","default","editor","emails","locale","manager","manager","submission"]

print('copy untransalted msgstr from en to fa')
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
print()
print('copy unkhown msgstr in fa from en')
for file in files:
    fa_pofile = polib.pofile(f'locale/fa/{file}.po')
    en_pofile = polib.pofile(f'locale/en/{file}.po')

    for entry in en_pofile:
        fa_found = fa_pofile.find(entry.msgid)
        if fa_found is None:
            fa_pofile.append(entry)
    fa_pofile.save()
    print(f'file {file} done')
