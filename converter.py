import pathlib
import logging

tcshrc_path = pathlib.Path.home() / '.tcshrc'
bashrc_path = pathlib.Path.home() / '.bashrc'


def alias_converter(tcshrc_text):
    tcshrc_contents = tcshrc_text.split()
    if len(tcshrc_contents) != 3:
        logging.warn(f"tcshrc alias not in the right format. Content: {tcshrc_text}")
        tcshrc_contents[2] = " ".join(tcshrc_contents[2:])
    return f"{tcshrc_contents[0]} {tcshrc_contents[1]}={tcshrc_contents[2]}\n"


def setenv_converter(tcshrc_text):
    tcshrc_text = tcshrc_text.split()
    if len(tcshrc_text) != 3:
        raise Exception(f"tcshrc setenv not in the right format. Content {tcshrc_text}")
    return f"export {tcshrc_text[1]}={tcshrc_text[2]}\n"


full_content = []
def main():
    with open(tcshrc_path, 'r') as tcshrc_handle:
        for cnt, content in enumerate(tcshrc_handle):
            print("Line {}: {}".format(cnt, content))
            if content.startswith("alias") is True:
                full_content.append(alias_converter(content))
            elif content.startswith("setenv") is True:
                full_content.append(setenv_converter(content))
            else:
                full_content.append(content)

    with open(bashrc_path, "w") as bashrc_file_handle:
        for line in full_content:
            bashrc_file_handle.write(line)






if __name__ == "__main__":
    main()