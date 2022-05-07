class ArrivalsAndDeparturesAnulation(Exception):
    
    def __init__(self: object, message: str = """
    It's not possible to search only_arrivals and
    only_departures at the same time.
    """):            
        super().__init__(message)
