#include "../include/Source.h"

void Source::generateDefault(){
    // points = {0,1,2},{0,0,0},{0,0,0}
    points.generate(3,3);
    points.insert(0,1,1);
    points.insert(0,2,2);
    // unit = {0,0,0},{0,0,0},{1,1,1}
    unit.generate(3,3);
    unit.insert(2,0,1);
    unit.insert(2,1,1);
    unit.insert(2,2,1);

    // the matrix class construction might have to be fairly empty,
    // and setting of the actual values might have to happen as a method
    // the local matrix values in matrix class should be set by a constructor
    numRays = 3;
};

Matrix Source::getPoints() {
    return points;
};

Matrix Source::getUnit() {
    return unit;
};

int Source::getNumRays() {
    return numRays;
};
