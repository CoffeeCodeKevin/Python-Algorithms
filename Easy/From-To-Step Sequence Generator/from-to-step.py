def generator(From, To, Step):
    if From == To and Step == 1:
        return [From]
    if Step == 0:
        return []
    if From < To:
        return range(From, To+1, Step)
    if To < From:
        return range(From, To-1, -Step)
