from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import tle2czml
from astrolibrary.utils.graphic.czml_maker import CzmlMaker


def convert_datetime(str_datetime):
    return datetime.strptime(str_datetime, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=ZoneInfo("UTC")
    )


def write_tle(tles, input_tle_path):
    with open(input_tle_path, "w") as f:
        # for loop with 3 lines per iteration
        for curr_tle in tles:
            f.write(curr_tle.title_line + "\n")
            f.write(curr_tle.first_line + "\n")
            f.write(curr_tle.second_line + "\n")


def make_czml_of_conjunction(client, conjunction):
    # NORAD ID
    primary_id_of_target_conjunction = conjunction.primary_id
    seconday_id_of_target_conjunction = conjunction.secondary_id

    # TCA
    tca_of_target_conjunction = convert_datetime(conjunction.tca)

    # ENTERING TIME (< THRESHOLD)
    entering_time_of_target_conjunction = convert_datetime(conjunction.entering_time)

    # LEAVING TIME (> THRESHOLD)
    leaving_time_of_target_conjunction = convert_datetime(conjunction.leaving_time)

    # DCA
    dca_of_target_conjunction = conjunction.dca

    # download_time_of_TLE
    download_time_of_TLE = convert_datetime(conjunction.download_time_of_TLE)

    # TLEs
    tle_of_primary_of_target_conjunction = client.tle_API.get_tle_by_norad_id_and_date(
        primary_id_of_target_conjunction, download_time_of_TLE
    )
    tle_of_secondary_of_target_conjunction = (
        client.tle_API.get_tle_by_norad_id_and_date(
            seconday_id_of_target_conjunction, download_time_of_TLE
        )
    )
    tles_of_pair = (
        tle_of_primary_of_target_conjunction + tle_of_secondary_of_target_conjunction
    )

    input_target_TLE_path = "target.tle"
    output_target_CZML_path = "target.czml"
    write_tle(tles_of_pair, input_target_TLE_path)

    output_target_CZML_path = "target.czml"
    tle2czml.create_czml(
        inputfile_path=input_target_TLE_path,
        start_time=tca_of_target_conjunction - timedelta(hours=1),
        end_time=tca_of_target_conjunction + timedelta(hours=1),
        outputfile_path=output_target_CZML_path,
        propagation_time_step_seconds=60,
    )

    czml = CzmlMaker.czml_prettier(
        output_target_CZML_path,
        draw_label=True,
        draw_path=True,
        interpolation_algrorithm="LAGRANGE",
        outline_width=1,
        pixel_size=1,
        outline_color=[0, 255, 0, 255],
    )

    conjunction_packet = CzmlMaker.make_conjunction_packet(conjunction=conjunction)
    czml.append(conjunction_packet)

    CzmlMaker.set_current_time(czml, entering_time_of_target_conjunction.isoformat())
    CzmlMaker.write_czml(output_target_CZML_path, czml)

    return czml


def make_czml_of_collision_avoidance_result(
    client, satellite_name, tca, collision_avoidance_result
):
    start_time_of_cola = convert_datetime(collision_avoidance_result.start_time_of_cola)
    end_time_of_cola = convert_datetime(collision_avoidance_result.end_time_of_cola)
    download_time_of_TLE = convert_datetime(
        collision_avoidance_result.download_time_of_TLE
    )

    secondary_ids = []

    for curr_conjunction in collision_avoidance_result.collision_avoidance_db:
        secondary_ids.append(curr_conjunction.secondary_id)

    tles_of_satellites = []

    for curr_norad_id in secondary_ids:
        curr_tle = client.tle_API.get_tle_by_norad_id_and_date(
            curr_norad_id, download_time_of_TLE
        )
        tles_of_satellites.append(curr_tle[0])

    input_target_TLE_path = "collision-avoidance.tle"
    output_target_CZML_path = "collision-avoidance.czml"
    with open(input_target_TLE_path, "w") as f:
        # for loop with 3 lines per iteration
        for curr_tle in tles_of_satellites:
            f.write(curr_tle.title_line + "\n")
            f.write(curr_tle.first_line + "\n")
            f.write(curr_tle.second_line + "\n")

    tle2czml.create_czml(
        inputfile_path=input_target_TLE_path,
        start_time=start_time_of_cola,
        end_time=end_time_of_cola,
        outputfile_path=output_target_CZML_path,
        propagation_time_step_seconds=60,
    )

    czml = CzmlMaker.czml_prettier(
        output_target_CZML_path,
        draw_label=True,
        draw_path=True,
        interpolation_algrorithm="LAGRANGE",
        outline_width=1,
        pixel_size=1,
        outline_color=[0, 255, 0, 255],
    )

    candidate_paths = collision_avoidance_result.candidate_paths

    orginal_trajectory_packet = (
        CzmlMaker.make_trajectory_packet_from_trajectory_url_for_cola(
            trajectory_id=0,
            trajectory_name=f"Original Trajectory ({satellite_name})",
            trajectory_url=candidate_paths[0],
            download_time_of_TLE=download_time_of_TLE.isoformat(),
            start_time_of_cola=start_time_of_cola.isoformat(),
            end_time_of_cola=end_time_of_cola.isoformat(),
            rgba=[255, 0, 0, 255],
        )
    )
    czml.append(orginal_trajectory_packet)

    for i in range(1, len(candidate_paths)):
        curr_trajectory_packet = (
            CzmlMaker.make_trajectory_packet_from_trajectory_url_for_cola(
                trajectory_id=i,
                trajectory_name="Candidate Path " + str(i),
                trajectory_url=candidate_paths[i],
                download_time_of_TLE=download_time_of_TLE.isoformat(),
                start_time_of_cola=start_time_of_cola.isoformat(),
                end_time_of_cola=end_time_of_cola.isoformat(),
                rgba=[0, 0, 255, 255],
            )
        )
        czml.append(curr_trajectory_packet)

    for curr_conjunction in collision_avoidance_result.collision_avoidance_db:
        primary_id_of_conjunction = curr_conjunction.primary_id
        secondary_id_of_conjunction = curr_conjunction.secondary_id
        entering_time = convert_datetime(curr_conjunction.entering_time)
        leaving_time = convert_datetime(curr_conjunction.leaving_time)
        pair_packet = CzmlMaker.make_pair_packet(
            primary_id_of_conjunction,
            secondary_id_of_conjunction,
            (entering_time - timedelta(seconds=2)).isoformat(),
            (leaving_time + timedelta(seconds=2)).isoformat(),
            rgba=[255, 0, 0, 255],
        )
        czml.append(pair_packet)

    czml = CzmlMaker.set_current_time(czml, convert_datetime(tca).isoformat())
    CzmlMaker.write_czml(output_target_CZML_path, czml)

    return czml


def make_czml_of_watcher_catcher_result(client, watcher_catcher_result):
    norad_ids_of_satellites = set()
    for curr_watching_time_interval in watcher_catcher_result.watching_time_interval:
        # print(f"watching_time_interval: {curr_watching_time_interval}")
        norad_ids_of_satellites.add(curr_watching_time_interval.secondary_id)

    download_time_of_TLE = convert_datetime(watcher_catcher_result.download_time_of_TLE)

    tles_of_satellites = []

    total_tle = client.tle_API.get_tle_by_date(download_time_of_TLE)
    for current_tle in total_tle:
        norad_id = int(current_tle.first_line[2:7])
        if norad_id in norad_ids_of_satellites:
            tles_of_satellites.append(current_tle)

    start_time_of_timeline = convert_datetime(
        watcher_catcher_result.start_time_of_timeline
    )
    end_time_of_timeline = convert_datetime(watcher_catcher_result.end_time_of_timeline)
    input_target_TLE_path = "watcher-catcher.tle"
    with open(input_target_TLE_path, "w") as f:
        # for loop with 3 lines per iteration
        for curr_tle in tles_of_satellites:
            f.write(curr_tle.title_line + "\n")
            f.write(curr_tle.first_line + "\n")
            f.write(curr_tle.second_line + "\n")

    input_target_TLE_path = "watcher-catcher.tle"
    output_target_CZML_path = "watcher-catcher.czml"
    tle2czml.create_czml(
        inputfile_path=input_target_TLE_path,
        start_time=start_time_of_timeline,
        end_time=end_time_of_timeline,
        outputfile_path=output_target_CZML_path,
        propagation_time_step_seconds=60,
    )

    from astrolibrary.utils.graphic.czml_maker import CzmlMaker

    czml = CzmlMaker.czml_prettier(
        output_target_CZML_path,
        draw_label=False,
        draw_path=False,
        interpolation_algrorithm="LAGRANGE",
        outline_width=1,
        pixel_size=1,
        outline_color=[0, 255, 0, 255],
    )
    fixed_site_packet = CzmlMaker.make_fixed_site_packet(
        site_id=0,
        start_time=start_time_of_timeline.isoformat(),
        end_time=end_time_of_timeline.isoformat(),
        latitude=watcher_catcher_result.apex_latitude,
        longitude=watcher_catcher_result.apex_longitude,
    )
    czml.append(fixed_site_packet)
    fixed_cone_packet = CzmlMaker.make_fixed_cone_packet(
        cone_id=0,
        start_time=start_time_of_timeline.isoformat(),
        end_time=end_time_of_timeline.isoformat(),
        latitude=watcher_catcher_result.apex_latitude,
        longitude=watcher_catcher_result.apex_longitude,
        cone_range=watcher_catcher_result.cone_range,
        cone_field_of_view=watcher_catcher_result.cone_field_of_view,
    )
    czml.append(fixed_cone_packet)

    for curr_watching_time_interval in watcher_catcher_result.watching_time_interval:
        start_time_of_time_interval = convert_datetime(
            curr_watching_time_interval.start_time_of_time_interval
        )
        end_time_of_time_interval = convert_datetime(
            curr_watching_time_interval.end_time_of_time_interval
        )
        pair_packet = CzmlMaker.make_pair_packet(
            "site_0",
            curr_watching_time_interval.secondary_id,
            start_time_of_time_interval.isoformat(),
            end_time_of_time_interval.isoformat(),
            rgba=[255, 0, 0, 255],
        )
        czml.append(pair_packet)

    CzmlMaker.write_czml(output_target_CZML_path, czml)

    return czml
