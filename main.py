import json
from datetime import datetime


def convertFromFormat1(jsonObject):
    locationParts = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }


def convertFromFormat2(jsonObject):
    timestamp = jsonObject["timestamp"]
    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    timestampMilliseconds = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestampMilliseconds,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }


def main():
     with open("data-1.json", encoding="utf-8") as f:
        jsonObject1 = json.load(f)

     with open("data-2.json", encoding="utf-8") as f:
        jsonObject2 = json.load(f)

     with open("data-result.json", encoding="utf-8") as f:
        expectedResult = json.load(f)

     result1 = convertFromFormat1(jsonObject1)
     result2 = convertFromFormat2(jsonObject2)

     assert result1 == expectedResult
     assert result2 == expectedResult

     print("All tests passed successfully!")


if __name__ == "__main__":
    main()