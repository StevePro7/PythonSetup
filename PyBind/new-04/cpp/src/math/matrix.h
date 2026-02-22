#pragma once
#include "vector.h"
#include <array>

namespace math {

class Matrix3 {
public:
    // Row-major storage
    std::array<double, 9> data;

    Matrix3();  // identity
    Matrix3(std::array<double,9> values);

    static Matrix3 identity();
    static Matrix3 rotationX(double radians);
    static Matrix3 rotationY(double radians);
    static Matrix3 rotationZ(double radians);

    double operator()(int row, int col) const;
    double& operator()(int row, int col);

    Matrix3 operator*(const Matrix3& other) const;
    Vector3 operator*(const Vector3& v) const;

    Matrix3 transpose() const;
};

}