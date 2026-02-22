find_package(GTest REQUIRED)

add_executable(runTests
    test_vector.cpp
    test_mesh.cpp
)

target_link_libraries(runTests
    GTest::gtest
    GTest::gmock
    meshcore
)

enable_testing()
add_test(NAME AllTests COMMAND runTests)