import json
import math


STARLINK_NORAD_ID = []
ONEWEB_NORAD_ID = []
O3B_NORAD_ID = []
HAWK_NORAD_ID = []
INTERSECTED_NORAD_ID = []
SECOND_ID = set()


class CzmlMaker:
    def __init__(self):
        pass

    def czml_prettier(
        czml_path,
        draw_label=False,
        draw_path=False,
        interpolation_algrorithm="LAGRANGE",
        outline_width=1,
        pixel_size=2,
        outline_color=[0, 255, 0, 255],
    ):
        with open(czml_path, "r") as f:
            json_data = f.read()
            json_data = json.loads(json_data)

        will_removed_data = []

        for i, json_datum in enumerate(json_data):
            if "clock" in json_datum:
                json_datum["clock"]["multiplier"] = 5
                json_datum["clock"]["range"] = "LOOP_STOP"
            if "billboard" in json_datum:
                json_datum.pop("billboard", None)

            if "label" in json_datum:
                if draw_label == False:
                    json_datum.pop("label", None)
                else:
                    pass

            if "path" in json_datum:
                for path_datum in json_datum["path"]["show"]:
                    path_datum["boolean"] = draw_path
                # json_datum.pop("path", None)
                json_datum["point"] = {
                    "color": {"rgba": [255, 255, 255, 255]},
                    "outlineColor": {"rgba": outline_color},
                    "outlineWidth": outline_width,
                    "pixelSize": pixel_size,
                }

            if "position" in json_datum:
                json_datum["position"][
                    "interpolationAlgorithm"
                ] = interpolation_algrorithm
                if interpolation_algrorithm == "LAGRANGE":
                    json_datum["position"]["interpolationDegree"] = 5
                else:
                    json_datum["position"]["interpolationDegree"] = 1
                    json_datum["id"] = json_datum["id"] + "_LINEAR"
                for data in json_datum["position"]["cartesian"]:
                    if math.isnan(data):
                        # print(json_data[json_datum])
                        if json_datum in json_data:
                            will_removed_data.append(json_datum)
                            # json_data.remove(json_datum)
                            break

        for removed_datum in will_removed_data:
            if removed_datum in json_data:
                json_data.remove(removed_datum)

        return json_data

    def remove_document(czml):
        for i, packet in enumerate(czml):
            if "document" in packet:
                czml.remove(packet)
        return czml

    def color_coding_by_name_and_find_set(
        czml,
        target_name,
        outline_color=[255, 255, 255, 255],
        outline_width=1,
        pixel_size=4,
    ):
        target_set = set()
        for i, packet in enumerate(czml):
            if "description" in packet:
                sat_name = packet["description"]
                if is_included_target_name_in_sat_name(target_name, sat_name):
                    target_set.add(packet["id"])
                    packet["point"] = {
                        "color": {"rgba": [255, 255, 255, 255]},
                        "outlineColor": {"rgba": outline_color},
                        "outlineWidth": outline_width,
                        "pixelSize": pixel_size,
                    }
        return czml, target_set

    def is_included_target_name_in_sat_name(target_name, sat_name):
        return target_name in sat_name

    def color_coding_by_id(
        czml,
        target_set,
        outline_color=[255, 255, 255, 255],
        color=[255, 255, 255, 255],
        outline_width=4,
        pixel_size=5,
    ):
        for i, packet in enumerate(czml):
            if "description" in packet:
                sat_name = packet["description"]
                if packet["id"] in target_set:
                    packet["point"] = {
                        "color": {"rgba": color},
                        "outlineColor": {"rgba": outline_color},
                        "outlineWidth": outline_width,
                        "pixelSize": pixel_size,
                    }
        return czml

    def write_czml(czml_path, czml):
        indented_czml = open(f"{czml_path}", "w")
        indented_czml.write(json.dumps(czml, indent=2))
        indented_czml.close()

    def add_ball(czml, target_satellite_id, start_time, end_time, length, rgba):
        target_ball_packet = {
            "id": f"ball#{target_satellite_id}",
            "name": f"Orbital ball#{target_satellite_id}",
            "availability": f"{start_time}/{end_time}",
            "description": f"Orbital ball#{target_satellite_id}",
            "position": {
                "reference": f"{target_satellite_id}#position",
            },
            "ellipsoid": {
                "radii": {
                    "cartesian": [length, length, length],
                },
                "fill": True,
                "material": {
                    "solidColor": {
                        "color": {
                            "rgba": rgba,
                        },
                    },
                },
            },
        }
        czml.append(target_ball_packet)
        return czml

    def add_cone(
        czml, target_satellite_id, start_time, end_time, delay, length, fov_deg, rgba
    ):
        pos = []
        for i, packet in enumerate(czml):
            if target_satellite_id == packet["id"]:
                pos = packet["position"]["cartesian"]

        n = len(pos) // 4  # ����Ʈ�� ���̸� 4�� ���� ���� ���մϴ�.

        moved_pos = []
        for i in range(n):
            start = i * 4  # ���� �ܰ迡�� �����ϴ� �ε���
            end = start + 4  # ���� �ܰ迡�� ������ �ε���
            sublist = pos[start:end]  # ���� �ܰ迡�� ó���� ���긮��Ʈ
            tick = sublist[0]
            x = sublist[1]
            y = sublist[2]
            z = sublist[3]

            magnitude = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))

            x = x - ((x / magnitude) * length) / 2
            y = y - ((y / magnitude) * length) / 2
            z = z - ((z / magnitude) * length) / 2
            moved_pos.append(tick)
            moved_pos.append(x)
            moved_pos.append(y)
            moved_pos.append(z)
        epoch_time = start_time.isoformat()
        start_time += delay
        start_time = start_time.isoformat()
        end_time = end_time.isoformat()
        target_cone_packet = {
            "id": f"cone#{target_satellite_id}",
            "name": f"Orbital Cone#{target_satellite_id}",
            "availability": f"{start_time}/{end_time}",
            "description": f"Orbital Cone#{target_satellite_id}",
            "position": {
                "epoch": f"{epoch_time}",
                "cartesian": moved_pos,
                "interpolationAlgorithm": "LAGRANGE",
                "interpolationDegree": 5,
                "referenceFrame": "INERTIAL",
            },
            "cylinder": {
                "length": length,
                "topRadius": 0.0,
                "bottomRadius": math.tan((fov_deg * math.pi) / 360) * length,
                "material": {
                    "solidColor": {
                        "color": {
                            "rgba": rgba,
                        },
                    },
                },
            },
        }
        czml.append(target_cone_packet)
        return czml

    def add_fixed_site(czml, site_id, start_time, end_time, x, y, z):
        print(site_id)
        site_packet = {
            "id": f"{site_id}",
            "name": "Site",
            "availability": f"{start_time.isoformat()}/{end_time.isoformat()}",
            "description": "Site",
            "label": {
                "fillColor": {
                    "rgba": [255, 255, 255, 255],
                },
                "font": "12pt Arial",
                "horizontalOrigin": "LEFT",
                "outlineColor": {
                    "rgba": [24, 24, 24, 255],
                },
                "outlineWidth": 2,
                "pixelOffset": {
                    "cartesian2": [10, 10],
                },
                "show": True,
                "style": "FILL_AND_OUTLINE",
                # "text": "Site",
                "text": f"{site_id}",  # Show site_id as the label text
                "verticalOrigin": "CENTER",
            },
            "position": {
                "referenceFrame": "FIXED",
                "epoch": f"{start_time.isoformat()}",
                "cartesian": [x, y, z],
            },
            "point": {
                "show": True,
                "color": {
                    "rgba": [255, 255, 255, 255],
                },
                "outlineColor": {
                    "rgba": [255, 0, 255, 255],
                },
                "outlineWidth": 4,
                "pixelSize": 8,
            },
        }

        czml.append(site_packet)
        return czml

    def add_fixed_cone(
        czml,
        cone_id,
        start_time,
        end_time,
        x,
        y,
        z,
        cone_range,
        cone_field_of_view,
        rgba=[240, 240, 24, 90],
    ):
        magnitude = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
        meter_cone_range = cone_range * 1000

        cone_packet = {
            "id": f"cone_{cone_id}",
            "name": "Site Cone",
            "availability": f"{start_time.isoformat()}/{end_time.isoformat()}",
            "description": "Site Cone",
            "position": {
                "referenceFrame": "FIXED",
                "cartesian": [
                    x + ((x / magnitude) * meter_cone_range) / 2,
                    y + ((y / magnitude) * meter_cone_range) / 2,
                    z + ((z / magnitude) * meter_cone_range) / 2,
                ],
            },
            "cylinder": {
                "length": meter_cone_range,
                "topRadius": math.tan((cone_field_of_view * math.pi) / 360)
                * meter_cone_range,
                "bottomRadius": 0.0,
                "material": {
                    "solidColor": {
                        "color": {
                            "rgba": rgba,
                        },
                    },
                },
            },
        }
        czml.append(cone_packet)
        return czml

    def add_pair(czml, pair_dict):
        for pair_key, interval_values in pair_dict.items():
            pid, sid = pair_key

            start_time_list = []
            tca_time_list = []
            end_time_list = []
            availability_set = []
            color_set = []
            rgba_before = [255, 0, 0, 255]
            rgba_intersected = [255, 0, 0, 255]
            rgba_after = [0, 0, 255, 255]
            for interval_value in interval_values:
                start_time, tca_time, end_time = interval_value
                start_time_list.append(start_time)
                tca_time_list.append(tca_time_list)
                end_time_list.append(end_time)
                availability_set.append(f"{start_time}/{end_time}")
                color_set.append(
                    {
                        "interval": f"{start_time}/{tca_time}",
                        "rgba": rgba_before,
                    },
                )
                color_set.append(
                    {
                        "interval": f"{tca_time}/{end_time}",
                        "rgba": rgba_after,
                    },
                )
            pair_packet = {
                "id": f"{pid}/{sid}",
                "name": f"{pid} to {sid}",
                "availability": availability_set,
                "polyline": {
                    "show": True,
                    "width": 3,
                    "material": {
                        "polylineOutline": {
                            "color": color_set,
                            "outlineColor": {
                                "rgba": [255, 255, 255, 255],
                            },
                            "outlineWidth": 1,
                        },
                    },
                    "arcType": "NONE",
                    "positions": {
                        "references": [f"{pid}#position", f"{sid}#position"],
                    },
                },
            }
            czml.append(pair_packet)

        return czml

    def rgba_reverse(rgba):
        opposite_rgba = []
        if len(rgba) == 3:
            opposite_rgba.append(abs(255 - rgba[0]))
            opposite_rgba.append(abs(255 - rgba[1]))
            opposite_rgba.append(abs(255 - rgba[2]))
            opposite_rgba.append(255)
        else:
            opposite_rgba.append(abs(255 - rgba[0]))
            opposite_rgba.append(abs(255 - rgba[1]))
            opposite_rgba.append(abs(255 - rgba[2]))
            opposite_rgba.append(rgba[3])
        return opposite_rgba

    def rgb_with_alpha(rgb, alpha):
        rgba = []
        rgba.append(rgb[0])
        rgba.append(rgb[1])
        rgba.append(rgb[2])
        rgba.append(alpha)

        return rgba

    def add_pair_for_RFI(czml, sites_and_targets, sites_and_colors, pair_dict):
        for pair_key, interval_values in pair_dict.items():
            pid, sid = pair_key

            start_time_list = []
            tca_time_list = []
            end_time_list = []
            availability_set = []
            color_set = []
            rgba_normal = [0, 0, 0, 255]
            rgba_interfered = [255, 0, 0, 255]
            rgba_target = [0, 0, 255, 255]

            for interval_value in interval_values:
                start_time, _, end_time, interfering = interval_value
                availability_set.append(f"{start_time}/{end_time}")

                for site, target_ids in sites_and_targets.items():
                    if sid in target_ids:
                        color = sites_and_colors[site]
                        color = rgb_with_alpha(color, 255)
                        color_set.append(
                            {
                                "interval": f"{start_time}/{end_time}",
                                "rgba": color,
                            },
                        )

                if interfering == "1":
                    for site, color in sites_and_colors.items():
                        if int(pid) == int(site[0]):
                            # rgba_interfered = rgba_reverse(color)
                            color_set.append(
                                {
                                    "interval": f"{start_time}/{end_time}",
                                    "rgba": rgba_interfered,
                                },
                            )
                else:
                    color_set.insert(
                        0,
                        {
                            "interval": f"{start_time}/{end_time}",
                            "rgba": rgba_normal,
                        },
                    )
            pair_packet = {
                "id": f"{pid}/{sid}",
                "name": f"{pid} to {sid}",
                "availability": availability_set,
                "polyline": {
                    "show": True,
                    "width": 3,
                    "material": {
                        "polylineOutline": {
                            "color": color_set,
                            "outlineColor": {
                                "rgba": [255, 255, 255, 255],
                            },
                            "outlineWidth": 1,
                        },
                    },
                    "arcType": "NONE",
                    "positions": {
                        "references": [f"{pid}#position", f"{sid}#position"],
                    },
                },
            }
            czml.append(pair_packet)

        return czml

    def add_trajectory(czml, filepath):
        f = open(filepath, "r")
        # check if f has extention as .e?
        if f.split(".")[1] == "e":
            for line in f.readlines():
                if line[0] == "#":
                    continue
                # is number?
                elif line[0].isdigit():
                    # 0 column: time, 1 column: x, 2 column: y, 3 column: z,
                    # 4 column: vx, 5 column: vy, 6 column: vz
                    line = line.split()
                    time = line[0]
                    x = line[1]
                    y = line[2]
                    z = line[3]
                    vx = line[4]
                    vy = line[5]
                    vz = line[6]
                else:
                    line = line.split()
                    if line[0] == "ScenarioEpoch":
                        epoch = line[1]
                    elif line[0] == "END":
                        break

    def remove_disinterested_set(czml, *interest_sets):
        will_removed_packet = []
        combined_set = set()
        for interest_set in interest_sets:
            combined_set = combined_set.union(interest_set)

        for i, packet in enumerate(czml):
            if "description" in packet:
                if packet["id"] in combined_set:
                    continue
                else:
                    will_removed_packet.append(packet)
                    # packet["show"] = False

        for removed_packet in will_removed_packet:
            if removed_packet in czml:
                czml.remove(removed_packet)

        return czml

    def check_intersect(pair_dict):
        result = {}
        for key, value in pair_dict.items():
            if key[1] in result:
                result[key[1]].append(key[0])
            else:
                result[key[1]] = [key[0]]

        print(result.keys())
        return result.keys()

    def read_ppdb(ppdb_path):
        primary_set = set()
        secondary_set = set()
        pair_dict = dict()
        src_file = open(ppdb_path, "r")
        assert src_file
        while input_line := src_file.readline():
            if input_line[0] == "%":
                continue

            (
                pid,
                sid,
                dca,
                tca,
                tca_start,
                tca_end,
                year,
                month,
                day,
                hour,
                minute,
                s,
                _,
            ) = input_line.split()

            second = int(float(s))

            microsecond = int(1000000 * (float(s) - int(float(s))))
            if second == 60:
                second = 59

            tca_time = datetime(
                int(year),
                int(month),
                int(day),
                int(hour),
                int(minute),
                second,
                microsecond,
                tzinfo=timezone.utc,
            )
            start_delta = timedelta(seconds=(float(tca_start) - float(tca)))
            end_delta = timedelta(seconds=(float(tca_end) - float(tca)))
            duration_delta = datetime.min + (end_delta - start_delta)
            start_time = (
                (tca_time + start_delta)
                # .astimezone(tz=timezone.utc)
                .isoformat(timespec="microseconds")
            )
            end_time = (
                (tca_time + end_delta)
                # .astimezone(tz=timezone.utc)
                .isoformat(timespec="microseconds")
            )
            duration = (
                duration_delta.time()
                # .astimezone(tz=timezone.utc)
                .isoformat(timespec="microseconds")
            )
            tca_time = tca_time.isoformat(timespec="microseconds")

            if (pid, sid) in pair_dict:
                pair_dict[(pid, sid)].append([start_time, tca_time, end_time])
            else:
                pair_dict[(pid, sid)] = [[start_time, tca_time, end_time]]
            primary_set.add(str(pid))
            secondary_set.add(str(sid))
        return pair_dict, primary_set, secondary_set

    def read_ppdb_for_RFI(ppdb_path):
        secondary_set = set()
        pair_dict = dict()
        src_file = open(ppdb_path, "r")
        assert src_file
        while input_line := src_file.readline():
            if input_line[0] == "%":
                continue

            (
                pid,
                sid,
                dca,
                tca,
                tca_start,
                tca_end,
                year,
                month,
                day,
                hour,
                minute,
                s,
                interfering,
                angle,
            ) = input_line.split()

            second = int(float(s))

            microsecond = int(1000000 * (float(s) - int(float(s))))
            if second == 60:
                second = 59

            tca_time = datetime(
                int(year),
                int(month),
                int(day),
                int(hour),
                int(minute),
                second,
                microsecond,
                tzinfo=timezone.utc,
            )
            start_delta = timedelta(seconds=(float(tca_start) - float(tca)))
            end_delta = timedelta(seconds=(float(tca_end) - float(tca)))
            duration_delta = datetime.min + (end_delta - start_delta)
            start_time = (
                (tca_time + start_delta)
                # .astimezone(tz=timezone.utc)
                .isoformat(timespec="microseconds")
            )
            end_time = (
                (tca_time + end_delta)
                # .astimezone(tz=timezone.utc)
                .isoformat(timespec="microseconds")
            )
            duration = (
                duration_delta.time()
                # .astimezone(tz=timezone.utc)
                .isoformat(timespec="microseconds")
            )
            tca_time = tca_time.isoformat(timespec="microseconds")

            if (pid, sid) in pair_dict:
                pair_dict[(pid, sid)].append(
                    [start_time, tca_time, end_time, interfering]
                )
            else:
                pair_dict[(pid, sid)] = [[start_time, tca_time, end_time, interfering]]

            secondary_set.add(str(sid))
        return pair_dict, secondary_set

    def merge_czml(czml1, czml2):
        for i, packet in enumerate(czml2):
            czml1.append(packet)
        return czml1

    def add_link(
        czml, start_time, end_time, start_id, end_id, output_link_optimization
    ):
        pair_packets = dict()
        for current_link in output_link_optimization:
            lo_current_time = current_link["loCurrentTime"]
            lo_path = current_link["path"]
            # make pair from start_id and end_id thru lo_path:
            for i in range(len(lo_path)):
                if i == 0:
                    pid = start_id
                    sid = lo_path[i]
                elif i == len(lo_path) - 1:
                    pid = lo_path[i]
                    sid = end_id
                else:
                    pid = lo_path[i - 1]
                    sid = lo_path[i]
                if (pid, sid) in pair_packets:
                    pair_packets[(pid, sid)] = append_availability(
                        pair_packets[(pid, sid)], lo_current_time, end_time
                    )
                else:
                    pair_packets[(pid, sid)] = pair_packet(pid, sid)

        czml.append(link_packet)
        return czml

    def pair_packet(pid, sid):
        pair_packet = {
            "id": f"{pid}/{sid}",
            "name": f"{pid} to {sid}",
            "availability": [],
            "polyline": {
                "show": True,
                "width": 3,
                "material": {
                    "polylineOutline": {
                        "color": [],
                        "outlineColor": {
                            "rgba": [255, 255, 255, 255],
                        },
                        "outlineWidth": 1,
                    },
                },
                "arcType": "NONE",
                "positions": {
                    "references": [f"{pid}#position", f"{sid}#position"],
                },
            },
        }
        return pair_packet

    def append_availability(pair_packet, start_time, end_time):
        pair_packet["availability"].append(f"{start_time}/{end_time}")
        return pair_packet

    def append_color(pair_packet, start_time, end_time, rgba):
        pair_packet["polyline"]["material"]["polylineOutline"]["color"].append(
            {
                "interval": f"{start_time}/{end_time}",
                "rgba": rgba,
            },
        )
        return pair_packet
