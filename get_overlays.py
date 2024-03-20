import json


CHAR_NAME = "Alex"

def read_overlays(jsonfile):
    # Read the JSON file
    print("Reading JSON file: %s" % jsonfile)
    overlay_names = []
    with open(jsonfile, 'r') as file:
        data = json.load(file)
        for overlay in data["TextureController"]["Overlays"]:
            overlay_names.append(overlay['CAT'])
    return overlay_names



def main():

    json_file_name = "./json_lookup_folder/"+CHAR_NAME+".json"
    # print(json_file_name)

    overlay_names = read_overlays(json_file_name)
    print(overlay_names)


if __name__ == "__main__":
    main()