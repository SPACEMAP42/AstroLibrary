import re


# TLE 파일에서 3le 정보 추출
def extract_3le(tle_file):
    with open(tle_file, "r") as f:
        tle_lines = f.readlines()
    tle_list = []
    for i in range(0, len(tle_lines), 3):
        name = tle_lines[i].strip()
        line1 = tle_lines[i + 1].strip()
        line2 = tle_lines[i + 2].strip()
        tle_list.append({"name": name, "line1": line1, "line2": line2})
    return tle_list


# TLE 파일에서 'O3b', 'Oneweb', 'Starlink' 중 하나를 포함하는 3le 정보 추출
def extract_3le_with_name(tle_file):
    tle_list = extract_3le(tle_file)
    pattern = re.compile("(O3B|ONEWEB|STARLINK)", re.IGNORECASE)
    output_list = []
    for tle in tle_list:
        name = tle["name"]
        match = pattern.search(name)
        if match:
            output_list.append(tle)
    return output_list


def write_3le_to_file(tle_list, output_file):
    with open(output_file, "w") as f:
        for tle in tle_list:
            f.write(tle["name"] + "\n")
            f.write(tle["line1"] + "\n")
            f.write(tle["line2"] + "\n")


tle_list = extract_3le_with_name(
    "/Users/shawn/develop/spacemap-assistant-tool/czmlmaker/2023-03-06-all.tle"
)

write_3le_to_file(tle_list, "output.tle")
