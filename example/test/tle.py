import astrolibrary

if __name__ == "__main__":
    spacemap = astrolibrary.Client(
        "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
    )
    print(spacemap.tle_API.get_tle_by_norad_id_and_date(39227))
    # tles = spacemap.tle_API.get_recent_tles()
    tles = spacemap.tle_API.get_tle_by_norad_id_and_date(39227)
    visualization_tool = astrolibrary.VisualizationTool()
    visualization_tool.draw_earth()
    visualization_tool.draw_tles_at_moment(tles)
    visualization_tool.show()
