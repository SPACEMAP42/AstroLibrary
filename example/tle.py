import astrolibrary

if __name__ == "__main__":
    spacemap = astrolibrary.client(
        "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
    )
    spacemap.token_auth.create_session()
    print(spacemap.tle.get_tle_by_norad_id_and_date(39227))
