# ---- GoogleTest ----
include(FetchContent)
FetchContent_Declare(
        googletest
        GIT_REPOSITORY https://github.com/google/googletest.git
        GIT_TAG v1.14.0
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# ---- Test executable ----
add_executable(tests_matrix test_matrix.cpp)
add_executable(tests_mesh_processor test_mesh_processor.cpp)
add_executable(tests_vector test_vector.cpp)

#add_executable(tests_mesh test_mesh.cpp)
#add_executable(tests_mesh_algorithms test_mesh_algorithms.cpp)
##        test_mesh_processor.cpp

# Ensure Python dev target is available for linking (Python C API symbols)
find_package(Python3 REQUIRED COMPONENTS Development)

target_link_libraries(tests_matrix
        PRIVATE
        my_api
        GTest::gtest_main
        Python3::Python
        )

target_link_libraries(tests_mesh_processor
        PRIVATE
        my_api
        GTest::gtest_main
        GTest::gmock_main
        Python3::Python
        )

target_link_libraries(tests_vector
        PRIVATE
        my_api
        GTest::gtest_main
        Python3::Python
        )

include(GoogleTest)
gtest_discover_tests(tests_matrix)
gtest_discover_tests(tests_mesh_processor)
gtest_discover_tests(tests_vector)
