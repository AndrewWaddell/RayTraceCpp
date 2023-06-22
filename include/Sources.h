#ifndef SOURCES_H
#define SOURCES_H

#include <vector>
#include "Source.h"
#include "Matrix.h"
#include <functional>

class Sources {
private:
    std::vector<Source> sources;
    Matrix matrix; // temporary multiuse matrix
public:
    void addSource(); // generates default source
    void addSource(const Source& source);
    Matrix points(); // returns points from all sources concatenated
    Matrix unit(); // returns all units from all sources concatenated
    int numRays(); // returns number of columns between sources
};

#endif
