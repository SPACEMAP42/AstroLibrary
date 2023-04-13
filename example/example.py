import astrolibrary

if __name__ == "__main__":
    
    # Create Astro Library Cilent
    spacemap = astrolibrary.Client(
        "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
    )
    
    # Token Auth API
    spacemap.token_auth_API.create_session()
    
    # # Watcher Catcher API
    # spacemap.watcher_catcher_API.predict_watcher_catcher()
    # # spacemap.watcher_catcher_API.get_requests_status_list()
    # id = spacemap.watcher_catcher_API.get_requests_status_list()['data'][-1]['_id']
    # print(spacemap.watcher_catcher_API.get_predicted_result(id))
    # # spacemap.watcher_catcher_API.delete_watcher_catcher_db_id(id)

    print(spacemap.watcher_catcher_API.predict_watcher_catcher_and_get_result())