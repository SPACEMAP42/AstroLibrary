import astrolibrary

if __name__ == "__main__":
    # Create Astro Library Cilent
    ROK_airforce = astrolibrary.Client(
        "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
    )

    # Conjunctions API
    print(ROK_airforce.conjunction_API.get_conjunctions())

    # # Watcher Catcher API
    # ROK_airforce.watcher_catcher_API.predict_watcher_catcher()
    # response = ROK_airforce.watcher_catcher_API.predict_watcher_catcher(altitude=2000)
    # print(response)
    print(ROK_airforce.watcher_catcher_API.get_requests_status_list())
    id = ROK_airforce.watcher_catcher_API.get_requests_status_list()["data"][-1]["_id"]
    print(ROK_airforce.watcher_catcher_API.get_predicted_result(id))
    # ROK_airforce.watcher_catcher_API.delete_watcher_catcher_db_id(id)

    # print(ROK_airforce.watcher_catcher_API.predict_watcher_catcher_and_get_result())
