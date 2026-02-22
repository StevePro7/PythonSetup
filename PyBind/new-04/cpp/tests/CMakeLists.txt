add_executable(runTests
    test_vector.cpp
    test_matrix.cpp
    test_mesh.cpp
    test_mesh_algorithms.cpp
    test_mesh_processor.cpp
)

target_link_libraries(runTests
    GTest::gtest
    GTest::gmock
    meshcore
)

enable_testing()
add_test(NAME AllTests COMMAND runTests)