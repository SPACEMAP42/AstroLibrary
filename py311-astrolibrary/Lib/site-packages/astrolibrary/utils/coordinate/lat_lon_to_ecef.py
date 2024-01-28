import pyproj


def convert_lat_lon_to_ecef(latitude, longitude):
    # WGS84 좌표계와 ECEF 좌표계 간의 변환을 위한 프로젝션 생성
    wgs84 = pyproj.Proj(proj="latlong", datum="WGS84", ellps="WGS84")
    ecef = pyproj.Proj(proj="geocent", datum="WGS84", ellps="WGS84")

    # WGS84 좌표를 ECEF 좌표로 변환
    x, y, z = pyproj.transform(wgs84, ecef, longitude, latitude, 0, radians=False)

    return x, y, z
