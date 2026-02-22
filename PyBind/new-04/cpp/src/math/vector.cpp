#include "vector.h"

namespace math {

Vector3::Vector3() : x(0), y(0), z(0) {}
Vector3::Vector3(double x, double y, double z) : x(x), y(y), z(z) {}

double Vector3::norm() const {
    return std::sqrt(x*x + y*y + z*z);
}

Vector3 Vector3::normalized() const {
    double n = norm();
    return {x/n, y/n, z/n};
}

Vector3 Vector3::operator+(const Vector3& o) const {
    return {x+o.x, y+o.y, z+o.z};
}

Vector3 Vector3::operator-(const Vector3& o) const {
    return {x-o.x, y-o.y, z-o.z};
}

Vector3 Vector3::operator*(double s) const {
    return {x*s, y*s, z*s};
}

double Vector3::dot(const Vector3& a, const Vector3& b) {
    return a.x*b.x + a.y*b.y + a.z*b.z;
}

Vector3 Vector3::cross(const Vector3& a, const Vector3& b) {
    return {
        a.y*b.z - a.z*b.y,
        a.z*b.x - a.x*b.z,
        a.x*b.y - a.y*b.x
    };
}

}