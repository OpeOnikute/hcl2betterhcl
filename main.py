import re

def run():

    output = ""

    with open("hcl.txt", "r") as file:
        for line in file:
            search_text_bracket = r"\"(.*)\" = (\{)"
            search_text_word = r"\"(.*)\" = ([\\\"\w\d\s\'\-\:\(\)\.\*\$\,\{\}\[\]\/\%\#\;\&\^\@\!]+)"

            search_obj_bracket = re.search(search_text_bracket, line, re.I)
            search_obj_word = re.search(search_text_word, line, re.I)

            if search_obj_bracket:
                output += "{} {}\n".format(search_obj_bracket.group(1), search_obj_bracket.group(2))
            elif search_obj_word:
                output += "    {} = {}".format(search_obj_word.group(1), search_obj_word.group(2))
            else:
                if line.strip() != "":
                    output += line

        print(output)

if __name__ == "__main__":
    run()