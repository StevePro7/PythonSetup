#include "matrix.h"
#include <cmath>

namespace math {

Matrix3::Matrix3()
    : data{1,0,0,
           0,1,0,
           0,0,1} {}

Matrix3::Matrix3(std::array<double,9> values)
    : data(values) {}

Matrix3 Matrix3::identity() {
    return Matrix3();
}

Matrix3 Matrix3::rotationX(double r) {
    double c = std::cos(r);
    double s = std::sin(r);

    return Matrix3({
        1, 0,  0,
        0, c, -s,
        0, s,  c
    });
}

Matrix3 Matrix3::rotationY(double r) {
    double c = std::cos(r);
    double s = std::sin(r);

    return Matrix3({
         c, 0, s,
         0, 1, 0,
        -s, 0, c
    });
}

Matrix3 Matrix3::rotationZ(double r) {
    double c = std::cos(r);
    double s = std::sin(r);

    return Matrix3({
        c, -s, 0,
        s,  c, 0,
        0,  0, 1
    });
}

double Matrix3::operator()(int row, int col) const {
    return data[row * 3 + col];
}

double& Matrix3::operator()(int row, int col) {
    return data[row * 3 + col];
}

Matrix3 Matrix3::operator*(const Matrix3& o) const {
    Matrix3 result;

    for (int r = 0; r < 3; ++r) {
        for (int c = 0; c < 3; ++c) {
            result(r,c) = 0.0;
            for (int k = 0; k < 3; ++k) {
                result(r,c) += (*this)(r,k) * o(k,c);
            }
        }
    }

    return result;
}

Vector3 Matrix3::operator*(const Vector3& v) const {
    return {
        data[0]*v.x + data[1]*v.y + data[2]*v.z,
        data[3]*v.x + data[4]*v.y + data[5]*v.z,
        data[6]*v.x + data[7]*v.y + data[8]*v.z
    };
}

Matrix3 Matrix3::transpose() const {
    Matrix3 t;

    for (int r = 0; r < 3; ++r)
        for (int c = 0; c < 3; ++c)
            t(r,c) = (*this)(c,r);

    return t;
}

}