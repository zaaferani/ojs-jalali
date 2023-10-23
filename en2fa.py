import polib

files = ["admin","author","default","editor","emails","locale","manager","manager","submission"]

print('copy untransalted msgstr from en to fa')
for file in files:
    # Loop through each file
    # Load the Farsi and English PO files
    # Iterate through each entry in the Farsi PO file
    # If the Farsi entry msgstr is empty
    #   Find the corresponding English entry by msgid
    #   If found, copy the English msgstr to the Farsi entry
    # Save the modified Farsi PO file
    # Print a message when done with each file
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
