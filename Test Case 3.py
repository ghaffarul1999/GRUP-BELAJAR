
def sortDictionaryDesc():
    d = {"ani":80, "budi":70, "ana":55, "susi":75, "rudi":60}
    return sorted(d.items(),
        key=lambda x: x[1],
        reverse=True)

print(sortDictionaryDesc())

