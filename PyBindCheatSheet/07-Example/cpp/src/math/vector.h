#pragma once
#include <cmath>

namespace math {

class Vector3 {
public:
    double x, y, z;

    Vector3();
    Vector3(double x, double y, double z);

    double norm() const;
    Vector3 normalized() const;

    Vector3 operator+(const Vector3& other) const;
    Vector3 operator-(const Vector3& other) const;
    Vector3 operator*(double scalar) const;

    static double dot(const Vector3& a, const Vector3& b);
    static Vector3 cross(const Vector3& a, const Vector3& b);
};

}