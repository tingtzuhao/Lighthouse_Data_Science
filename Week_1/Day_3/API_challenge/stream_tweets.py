def main(FILTER, LANGUAGES, PATH):
    with open(PATH, 'a') as f:
        
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            f.write(json.dumps(line))
            f.write('\n')

main(FILTER, LANGUAGES, PATH)