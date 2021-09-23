cdef extern from "version.h":
    char* ios_get_version()

def get_version():
    return ios_get_version().decode('UTF-8')