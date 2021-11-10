import json
#TODO do not split {} by ,. We need a more deeper parser!
bib_list = {}
with open("qmlcourseRU/_bibliography/references.bib", "r") as bibfile:
    bibtex = bibfile.readlines()
    entry_type=None
    entry=None
    for line in bibtex:
        # print(line)
        line = line.strip() #remove spaces and tabs at start/end of line (trimm string)
        # print(line)
        if line.startswith("@"):
            if entry_type is not None:
                bib_list[entry_label] = {
                    #TODO: all variants
                    "entry_type":entry_type,
                    "entry_label":entry_label,
                    "entry":entry,
                    }

            entry_type, entry = line.split("{")
            entry_label, entry = entry.split(",")
            # entry = "{" + entry attepmt to use json.loads()
        else:
            entry+=line
print(bib_list)
with open("qmlcourseRU/_bibliography/references2.bib", "w") as bibfile:
    for k, v in bib_list.items():
        bibfile.writelines(v["entry_type"]+"{"+v["entry_label"]+",\n")
        split_entry_lines = v["entry"].split("},")
        for i in split_entry_lines[:-1]:
            bibfile.writelines(i+"},\n")
        bibfile.writelines(split_entry_lines[-1]+"\n")
